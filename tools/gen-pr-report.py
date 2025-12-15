#!/usr/bin/env python3
"""
Generate PR validation report from GitHub Actions data.

This script analyzes workflow runs and generates reports on:
- Students having trouble with the PR process
- Systematic errors (jobs that fail more than others)

Usage:
    # From GitHub Actions workflow (uses GITHUB_TOKEN)
    python3 generate-pr-report.py
    
    # From local machine (requires GITHUB_TOKEN env var or gh CLI)
    export GITHUB_TOKEN="github_pat_xxxxx"
    python3 generate-pr-report.py
    
    # Or use gh CLI authentication
    gh auth login
    python3 generate-pr-report.py

Environment Variables:
    GITHUB_TOKEN: GitHub personal access token or workflow token
    GITHUB_REPOSITORY: Repository in format "owner/repo" (auto-set in workflows)
    REPORT_DAYS: Number of days to analyze (default: 7)
"""

import os
import sys
import json
import requests
from collections import defaultdict
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


# Configuration
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "")
REPORT_DAYS = int(os.environ.get("REPORT_DAYS", "7"))

if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN environment variable not set", file=sys.stderr)
    print("Set it with: export GITHUB_TOKEN='your_token'", file=sys.stderr)
    print("Or authenticate with: gh auth login", file=sys.stderr)
    sys.exit(1)

if not GITHUB_REPOSITORY:
    print("Error: GITHUB_REPOSITORY environment variable not set", file=sys.stderr)
    print("Set it with: export GITHUB_REPOSITORY='owner/repo'", file=sys.stderr)
    sys.exit(1)

OWNER, REPO_NAME = GITHUB_REPOSITORY.split("/")


def get_pr_runs(days: int = 7) -> List[Dict]:
    """
    Get workflow runs from last N days.
    
    Args:
        days: Number of days to look back
        
    Returns:
        List of workflow run objects
    """
    since = (datetime.now() - timedelta(days=days)).isoformat()
    
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/actions/runs"
    params = {
        "event": "pull_request",
        "status": "completed",
        "per_page": 100
    }
    
    runs = []
    while url:
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            
            runs.extend(data["workflow_runs"])
            
            # Check for next page
            url = resp.links.get("next", {}).get("url")
            params = {}  # Params are in the next URL
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching workflow runs: {e}", file=sys.stderr)
            break
    
    # Filter by date
    return [r for r in runs if r["created_at"] >= since]


def get_pr_from_check_suite(run_id: int, check_suite_id: Optional[int]) -> Optional[int]:
    """
    Get PR number via check suite (Method 2 - most reliable).
    
    Args:
        run_id: Workflow run ID
        check_suite_id: Check suite ID from the run
        
    Returns:
        PR number or None if not found
    """
    if not check_suite_id:
        return None
    
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        # Get check suite details (includes PR refs)
        url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/check-suites/{check_suite_id}"
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
        check_suite = resp.json()
        
        # pull_requests array here is more reliable than in workflow runs
        if check_suite.get("pull_requests"):
            return check_suite["pull_requests"][0]["number"]
        
    except requests.exceptions.RequestException as e:
        print(f"Warning: Could not fetch check suite {check_suite_id}: {e}", file=sys.stderr)
    
    return None


def get_run_jobs(run_id: int) -> List[Dict]:
    """
    Get jobs for a specific workflow run.
    
    Args:
        run_id: Workflow run ID
        
    Returns:
        List of job objects
    """
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/actions/runs/{run_id}/jobs"
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
        return resp.json().get("jobs", [])
    except requests.exceptions.RequestException as e:
        print(f"Warning: Could not fetch jobs for run {run_id}: {e}", file=sys.stderr)
        return []


def analyze_failures(days: int = 7) -> Dict:
    """
    Analyze workflow failures and generate report data.
    
    Args:
        days: Number of days to analyze
        
    Returns:
        Dictionary with PR-grouped failure data
    """
    print(f"Fetching workflow runs from last {days} days...", file=sys.stderr)
    runs = get_pr_runs(days=days)
    print(f"Found {len(runs)} workflow runs", file=sys.stderr)
    
    # Group by PR using check suite method
    pr_data = defaultdict(lambda: {
        "username": None,
        "runs": [],
        "job_failures": defaultdict(int),
        "total_runs": 0,
        "failed_runs": 0
    })
    
    # Cache to avoid repeated API calls for same check suite
    check_suite_cache = {}
    runs_without_pr = 0
    
    for idx, run in enumerate(runs, 1):
        if idx % 10 == 0:
            print(f"Processing run {idx}/{len(runs)}...", file=sys.stderr)
        
        run_id = run["id"]
        check_suite_id = run.get("check_suite_id")
        
        # Get PR number via check suite (with caching)
        pr_number = None
        if check_suite_id:
            if check_suite_id not in check_suite_cache:
                check_suite_cache[check_suite_id] = get_pr_from_check_suite(run_id, check_suite_id)
            pr_number = check_suite_cache[check_suite_id]
        
        if not pr_number:
            runs_without_pr += 1
            continue
        
        # Get user info
        username = run.get("actor", {}).get("login", "unknown")
        pr_data[pr_number]["username"] = username
        pr_data[pr_number]["total_runs"] += 1
        
        # Get jobs for this run
        jobs = get_run_jobs(run_id)
        
        run_summary = {
            "run_id": run_id,
            "conclusion": run["conclusion"],
            "created_at": run["created_at"],
            "jobs": {}
        }
        
        run_failed = False
        for job in jobs:
            job_name = job["name"]
            job_conclusion = job["conclusion"]
            run_summary["jobs"][job_name] = job_conclusion
            
            if job_conclusion == "failure":
                pr_data[pr_number]["job_failures"][job_name] += 1
                run_failed = True
        
        if run_failed:
            pr_data[pr_number]["failed_runs"] += 1
        
        pr_data[pr_number]["runs"].append(run_summary)
    
    print(f"\nAnalysis complete:", file=sys.stderr)
    print(f"  - Mapped to PRs: {len(runs) - runs_without_pr}", file=sys.stderr)
    print(f"  - Could not map: {runs_without_pr}", file=sys.stderr)
    print(f"  - Unique PRs: {len(pr_data)}", file=sys.stderr)
    
    return dict(pr_data)


def print_report(pr_data: Dict, days: int = 7) -> None:
    """
    Print formatted report in Markdown.
    
    Args:
        pr_data: PR-grouped failure data
        days: Number of days analyzed
    """
    print(f"# PR Validation Report")
    print(f"\n**Period:** Last {days} days")
    print(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"**Repository:** {GITHUB_REPOSITORY}")
    
    if not pr_data:
        print("\n*No PR workflow data found in this period.*")
        return
    
    # Section 1: Students with most failures
    print("\n## Students With Most Failures")
    print("\nThis section identifies students who may need help with the PR process.\n")
    
    student_failures = []
    for pr_num, data in pr_data.items():
        total_failures = sum(data["job_failures"].values())
        if total_failures > 0:
            student_failures.append({
                "username": data["username"],
                "pr": pr_num,
                "failures": total_failures,
                "runs": data["total_runs"],
                "failed_runs": data["failed_runs"],
                "details": dict(data["job_failures"])
            })
    
    if not student_failures:
        print("*No failures detected - all PRs passed validation!* ✅")
    else:
        student_failures.sort(key=lambda x: x["failures"], reverse=True)
        
        print("| Student | PR | Failed Runs | Total Runs | Job Failures |")
        print("|---------|----|-----------:|----------:|--------------|")
        
        for student in student_failures[:15]:  # Top 15
            job_list = ", ".join([f"{job} ({count}x)" for job, count in 
                                 sorted(student['details'].items(), key=lambda x: x[1], reverse=True)])
            print(f"| {student['username']} | "
                  f"[#{student['pr']}](https://github.com/{GITHUB_REPOSITORY}/pull/{student['pr']}) | "
                  f"{student['failed_runs']} | "
                  f"{student['runs']} | "
                  f"{job_list} |")
    
    # Section 2: Jobs that fail most often
    print("\n## Jobs That Fail Most Often")
    print("\nThis section identifies systematic issues with specific validation jobs.\n")
    
    all_failures = defaultdict(int)
    all_runs = defaultdict(int)
    
    for data in pr_data.values():
        for run in data["runs"]:
            for job_name, conclusion in run["jobs"].items():
                all_runs[job_name] += 1
                if conclusion == "failure":
                    all_failures[job_name] += 1
    
    if not all_failures:
        print("*No job failures detected!* ✅")
    else:
        print("| Job Name | Failures | Total Runs | Failure Rate |")
        print("|----------|--------:|----------:|-------------:|")
        
        for job, count in sorted(all_failures.items(), key=lambda x: x[1], reverse=True):
            total = all_runs[job]
            rate = (count / total * 100) if total > 0 else 0
            print(f"| {job} | {count} | {total} | {rate:.1f}% |")
    
    # Section 3: Summary statistics
    print("\n## Summary Statistics")
    print()
    
    total_prs = len(pr_data)
    prs_with_failures = len([d for d in pr_data.values() if sum(d["job_failures"].values()) > 0])
    prs_all_pass = total_prs - prs_with_failures
    
    total_workflow_runs = sum(d["total_runs"] for d in pr_data.values())
    total_failed_runs = sum(d["failed_runs"] for d in pr_data.values())
    
    print(f"- **Total PRs analyzed:** {total_prs}")
    print(f"- **PRs with all runs passing:** {prs_all_pass} ({prs_all_pass/total_prs*100:.1f}%)" if total_prs > 0 else "")
    print(f"- **PRs with at least one failure:** {prs_with_failures} ({prs_with_failures/total_prs*100:.1f}%)" if total_prs > 0 else "")
    print(f"- **Total workflow runs:** {total_workflow_runs}")
    print(f"- **Failed workflow runs:** {total_failed_runs} ({total_failed_runs/total_workflow_runs*100:.1f}%)" if total_workflow_runs > 0 else "")
    
    # Most common failure jobs
    if all_failures:
        top_failing_job = max(all_failures.items(), key=lambda x: x[1])
        print(f"- **Most common failing job:** {top_failing_job[0]} ({top_failing_job[1]} failures)")


def main():
    """Main entry point."""
    try:
        print(f"\nGenerating PR Validation Report for {GITHUB_REPOSITORY}", file=sys.stderr)
        print(f"Analyzing last {REPORT_DAYS} days...\n", file=sys.stderr)
        
        data = analyze_failures(days=REPORT_DAYS)
        print_report(data, days=REPORT_DAYS)
        
    except KeyboardInterrupt:
        print("\n\nReport generation cancelled", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nError generating report: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
