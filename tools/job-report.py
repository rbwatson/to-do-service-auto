#!/usr/bin/env python3
"""Generate PR validation report from GitHub Actions data."""

import requests
import json
from collections import defaultdict
from datetime import datetime, timedelta

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "")
REPORT_DAYS = int(os.environ.get("REPORT_DAYS", "7"))


def get_pr_runs(days=7):
    """Get workflow runs from last N days."""
    since = (datetime.now() - timedelta(days=days)).isoformat()
    
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/actions/runs"
    params = {
        "event": "pull_request",
        "status": "completed",
        "per_page": 100
    }
    
    runs = []
    while url:
        resp = requests.get(url, headers=headers, params=params)
        data = resp.json()
        runs.extend(data["workflow_runs"])
        url = resp.links.get("next", {}).get("url")
    
    return [r for r in runs if r["created_at"] >= since]

def get_run_jobs(run_id):
    """Get jobs for a specific run."""
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/actions/runs/{run_id}/jobs"
    
    resp = requests.get(url, headers=headers)
    return resp.json()["jobs"]

def get_pr_for_run(run):
    """Get PR number for a workflow run."""
    # Method 1: Check pull_requests array first (sometimes populated)
    if run.get("pull_requests"):
        return run["pull_requests"][0]["number"]
    
    # Method 2: Parse from head_branch
    # PR branches often follow patterns like: pr-123, feature/fix, etc.
    head_branch = run.get("head_branch", "")
    head_sha = run.get("head_sha", "")
    
    # Query PRs to find matching branch
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/pulls"
    params = {"state": "all", "per_page": 100}
    
    resp = requests.get(url, headers=headers, params=params)
    prs = resp.json()
    
    for pr in prs:
        # Match by head branch and SHA
        if (pr["head"]["ref"] == head_branch and 
            pr["head"]["sha"] == head_sha):
            return pr["number"]
    
    return None


def analyze_failures():
    """Generate failure report."""
    runs = get_pr_runs(days=REPORT_DAYS)
    
    # Group by PR
    pr_data = defaultdict(lambda: {
        "username": None,
        "runs": [],
        "job_failures": defaultdict(int)
    })
    print (f"Analyzing {len(runs)} workflow runs...")
    for run in runs:
        if "pull_requests" not in run or not run["pull_requests"]:
            print(f"Skipping run {run['id']} with no associated PRs")
            pr_number = -1
        else:   
            pr_number = run.get("pull_requests", [{}])[0].get("number")
            if not pr_number:
                continue
         
        if "actor" in run and run["actor"]:
            username = run["actor"]["login"]
        else:
            username = run["head_repository"]["owner"]["login"]
        pr_data[pr_number]["username"] = username
        
        jobs = get_run_jobs(run["id"])
        run_summary = {
            "run_id": run["id"],
            "conclusion": run["conclusion"],
            "jobs": {}
        }
        
        for job in jobs:
            job_name = job["name"]
            job_conclusion = job["conclusion"]
            run_summary["jobs"][job_name] = job_conclusion
            
            if job_conclusion == "failure":
                pr_data[pr_number]["job_failures"][job_name] += 1
        
        pr_data[pr_number]["runs"].append(run_summary)
    
    return pr_data

def print_report(pr_data):
    """Print formatted report."""
    print("\n" + "="*80)
    print(f"PR VALIDATION REPORT - Last {REPORT_DAYS} Days")
    print("="*80)
    
    # Student struggles
    print("\n## Students With Most Failures\n")
    student_failures = []
    for pr_num, data in pr_data.items():
        total_failures = sum(data["job_failures"].values())
        if total_failures > 0:
            student_failures.append({
                "username": data["username"],
                "pr": pr_num,
                "failures": total_failures,
                "details": dict(data["job_failures"])
            })
    
    student_failures.sort(key=lambda x: x["failures"], reverse=True)
    
    for student in student_failures[:10]:
        print(f"\n{student['username']} (PR #{student['pr']}): {student['failures']} failures")
        for job, count in student['details'].items():
            print(f"  - {job}: {count}x")
    
    # Systematic failures
    print("\n\n## Jobs That Fail Most Often\n")
    all_failures = defaultdict(int)
    for data in pr_data.values():
        for job, count in data["job_failures"].items():
            all_failures[job] += count
    
    for job, count in sorted(all_failures.items(), key=lambda x: x[1], reverse=True):
        print(f"{job}: {count} failures")

if __name__ == "__main__":
    if requests is None:
        print("The 'requests' library is required. Please install it with 'pip install requests'.")
        exit(1)
    data = analyze_failures()
    print_report(data)
