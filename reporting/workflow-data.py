#!/usr/bin/env python3
"""
Query GitHub Actions workflow data for analysis and reporting.

Usage:
    workflow-data.py list-runs <owner> <repo> [options]
    workflow-data.py get-run <owner> <repo> <run-id>
    workflow-data.py list-jobs <owner> <repo> <run-id>
    workflow-data.py get-job <owner> <repo> <job-id>
    workflow-data.py timing <owner> <repo> <run-id>

Examples:
    # List recent workflow runs
    workflow-data.py list-runs rbwatson to-do-service-auto
    
    # List runs from last 14 days for specific workflow
    workflow-data.py list-runs rbwatson to-do-service-auto --days 14 --workflow pr-validation.yml
    
    # Get details for specific run
    workflow-data.py get-run rbwatson to-do-service-auto 12345678
    
    # List all jobs in a run
    workflow-data.py list-jobs rbwatson to-do-service-auto 12345678
    
    # Get detailed job information
    workflow-data.py get-job rbwatson to-do-service-auto 98765432
    
    # Get timing information for a run
    workflow-data.py timing rbwatson to-do-service-auto 12345678
"""

import sys
import json
import argparse
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from workflow_data_utils import (
    list_workflow_runs,
    get_workflow_run_details,
    list_workflow_jobs,
    get_workflow_job_details,
    get_workflow_run_timing
)


def output_json(data, pretty=True):
    """Output data as JSON."""
    if data is None:
        print("Error: No data to output", file=sys.stderr)
        sys.exit(1)
    
    if pretty:
        print(json.dumps(data, indent=2))
    else:
        print(json.dumps(data))


def cmd_list_runs(args):
    """List workflow runs."""
    runs = list_workflow_runs(
        repo_owner=args.owner,
        repo_name=args.repo,
        workflow_name=args.workflow,
        days_back=args.days,
        branch=args.branch,
        status=args.status
    )
    
    if runs is None:
        sys.exit(1)
    
    output_json(runs, pretty=not args.compact)


def cmd_get_run(args):
    """Get workflow run details."""
    details = get_workflow_run_details(
        repo_owner=args.owner,
        repo_name=args.repo,
        run_id=args.run_id
    )
    
    if details is None:
        sys.exit(1)
    
    output_json(details, pretty=not args.compact)


def cmd_list_jobs(args):
    """List jobs for a workflow run."""
    jobs = list_workflow_jobs(
        repo_owner=args.owner,
        repo_name=args.repo,
        run_id=args.run_id
    )
    
    if jobs is None:
        sys.exit(1)
    
    output_json(jobs, pretty=not args.compact)


def cmd_get_job(args):
    """Get job details."""
    job = get_workflow_job_details(
        repo_owner=args.owner,
        repo_name=args.repo,
        job_id=args.job_id
    )
    
    if job is None:
        sys.exit(1)
    
    output_json(job, pretty=not args.compact)


def cmd_timing(args):
    """Get timing information for a workflow run."""
    timing = get_workflow_run_timing(
        repo_owner=args.owner,
        repo_name=args.repo,
        run_id=args.run_id
    )
    
    if timing is None:
        sys.exit(1)
    
    output_json(timing, pretty=not args.compact)


def main():
    parser = argparse.ArgumentParser(
        description='Query GitHub Actions workflow data',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    subparsers.required = True
    
    # Common arguments
    def add_common_args(subparser):
        subparser.add_argument('owner', help='Repository owner')
        subparser.add_argument('repo', help='Repository name')
        subparser.add_argument('--compact', action='store_true',
                             help='Output compact JSON (no pretty-printing)')
    
    # list-runs command
    parser_list = subparsers.add_parser('list-runs',
                                        help='List workflow runs')
    add_common_args(parser_list)
    parser_list.add_argument('--workflow', default='pr-validation.yml',
                           help='Workflow file name (default: pr-validation.yml)')
    parser_list.add_argument('--days', type=int, default=7,
                           help='Days of history to retrieve (default: 7)')
    parser_list.add_argument('--branch',
                           help='Filter by branch name')
    parser_list.add_argument('--status',
                           choices=['completed', 'in_progress', 'queued'],
                           help='Filter by status')
    parser_list.set_defaults(func=cmd_list_runs)
    
    # get-run command
    parser_get = subparsers.add_parser('get-run',
                                       help='Get workflow run details')
    add_common_args(parser_get)
    parser_get.add_argument('run_id', type=int, help='Workflow run ID')
    parser_get.set_defaults(func=cmd_get_run)
    
    # list-jobs command
    parser_jobs = subparsers.add_parser('list-jobs',
                                        help='List jobs for a workflow run')
    add_common_args(parser_jobs)
    parser_jobs.add_argument('run_id', type=int, help='Workflow run ID')
    parser_jobs.set_defaults(func=cmd_list_jobs)
    
    # get-job command
    parser_job = subparsers.add_parser('get-job',
                                       help='Get job details')
    add_common_args(parser_job)
    parser_job.add_argument('job_id', type=int, help='Job ID')
    parser_job.set_defaults(func=cmd_get_job)
    
    # timing command
    parser_timing = subparsers.add_parser('timing',
                                          help='Get timing information for a run')
    add_common_args(parser_timing)
    parser_timing.add_argument('run_id', type=int, help='Workflow run ID')
    parser_timing.set_defaults(func=cmd_timing)
    
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
