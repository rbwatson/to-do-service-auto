#!/usr/bin/env python3
"""
Utilities for collecting GitHub Actions workflow data.

This module provides functions for:
- Fetching workflow runs and their details
- Retrieving job information and step-level data
- Querying workflow execution history
- Supporting workflow performance analysis

All functions use the GitHub CLI (gh) via bash commands.
"""

import json
import subprocess
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, List, Any
from urllib.parse import urlencode


def _check_gh_cli() -> bool:
    """
    Verify gh CLI is available and authenticated.
    
    Returns:
        True if gh CLI is available and authenticated, False otherwise
    """
    try:
        result = subprocess.run(
            ['gh', '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode != 0:
            print("Error: gh CLI not found. Install from https://cli.github.com/")
            return False
        
        # Check authentication
        result = subprocess.run(
            ['gh', 'auth', 'status'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode != 0:
            print("Error: gh CLI not authenticated. Run 'gh auth login'")
            return False
            
        return True
    except FileNotFoundError:
        print("Error: gh CLI not found. Install from https://cli.github.com/")
        return False
    except subprocess.TimeoutExpired:
        print("Error: gh CLI check timed out")
        return False
    except Exception as e:
        print(f"Error checking gh CLI: {e}")
        return False


def _run_gh_api(endpoint: str, params: Optional[Dict[str, str]] = None) -> Optional[Dict[str, Any]]:
    """
    Execute a gh api command and return parsed JSON response.
    
    Args:
        endpoint: GitHub API endpoint (e.g., '/repos/owner/repo/actions/runs')
        params: Optional query parameters as key-value pairs
        
    Returns:
        Parsed JSON response as dict, or None on error
        
    Note:
        Errors are logged but not raised. Caller should check for None.
    """
    if not _check_gh_cli():
        return None
    
    # Build URL with query parameters
    url = endpoint
    if params:
        query_string = urlencode(params)
        url = f"{endpoint}?{query_string}"
    
    cmd = ['gh', 'api', url]
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode != 0:
            print(f"Error: gh api failed: {result.stderr}")
            return None
        
        return json.loads(result.stdout)
        
    except subprocess.TimeoutExpired:
        print(f"Error: gh api request timed out for {endpoint}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON response: {e}")
        return None
    except Exception as e:
        print(f"Error running gh api: {e}")
        return None


def _filter_fields(data: Any, fields: Optional[List[str]]) -> Any:
    """
    Filter data to include only specified fields.
    
    Args:
        data: Data to filter (dict, list, or primitive)
        fields: List of field names to include, or None for all fields
        
    Returns:
        Filtered data with only specified fields
        
    Note:
        - Supports dot notation for nested fields (e.g., 'actor.login')
        - If field doesn't exist, it's omitted from output
        - Works recursively on lists
    """
    if fields is None:
        return data
    
    if isinstance(data, list):
        return [_filter_fields(item, fields) for item in data]
    
    if not isinstance(data, dict):
        return data
    
    filtered = {}
    for field in fields:
        # Support dot notation for nested fields
        if '.' in field:
            parts = field.split('.', 1)
            first, rest = parts[0], parts[1]
            if first in data:
                nested_value = data[first]
                if isinstance(nested_value, dict):
                    nested_filtered = _filter_fields(nested_value, [rest])
                    if rest in nested_filtered:
                        if first not in filtered:
                            filtered[first] = {}
                        filtered[first][rest] = nested_filtered[rest]
        else:
            # Simple field
            if field in data:
                filtered[field] = data[field]
    
    return filtered


def list_workflow_runs(
    repo_owner: str,
    repo_name: str,
    workflow_name: Optional[str] = None,
    days_back: int = 7,
    branch: Optional[str] = None,
    status: Optional[str] = None,
    fields: Optional[List[str]] = None
) -> Optional[List[Dict[str, Any]]]:
    """
    List workflow runs for a repository.
    
    Args:
        repo_owner: Repository owner (username or organization)
        repo_name: Repository name
        workflow_name: Optional workflow file name to filter results (e.g. 'pr-validation.yml')
                      If None, returns all workflows
        days_back: Number of days of history to retrieve (default: 7)
        branch: Optional branch name filter
        status: Optional status filter ('completed', 'in_progress', 'queued', etc.)
        fields: Optional list of field names to include in results
                Supports dot notation (e.g., ['id', 'name', 'actor.login'])
                If None, returns all fields
        
    Returns:
        List of workflow run dictionaries, or None on error
        Each dict contains: id, name, status, conclusion, created_at, html_url, etc.
        
    Example:
        >>> runs = list_workflow_runs('rbwatson', 'to-do-service-auto')
        >>> len(runs)
        15
        >>> runs[0]['conclusion']
        'success'
        
        >>> # Filter to specific workflow
        >>> runs = list_workflow_runs('rbwatson', 'to-do-service-auto', 
        ...                           workflow_name='pr-validation.yml')
        
        >>> # Return only specific fields
        >>> runs = list_workflow_runs('rbwatson', 'to-do-service-auto',
        ...                           fields=['id', 'name', 'conclusion'])
        >>> runs[0].keys()
        dict_keys(['id', 'name', 'conclusion'])
    """
    # Use general actions/runs endpoint (more reliable than workflow-specific)
    endpoint = f'/repos/{repo_owner}/{repo_name}/actions/runs'
    
    # Calculate date cutoff (timezone-aware)
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_back)
    created_filter = cutoff_date.strftime('%Y-%m-%dT%H:%M:%SZ')
    
    params = {
        'per_page': '100',
        'created': f'>={created_filter}'
    }
    
    if branch:
        params['branch'] = branch
    
    if status:
        params['status'] = status
    
    response = _run_gh_api(endpoint, params)
    if response is None:
        return None
    
    workflow_runs = response.get('workflow_runs', [])
    
    # Filter by date (GitHub's created filter sometimes returns more)
    filtered_runs = [
        run for run in workflow_runs
        if datetime.fromisoformat(run['created_at'].replace('Z', '+00:00')) >= cutoff_date
    ]
    
    # Filter by workflow name if specified
    if workflow_name:
        filtered_runs = [
            run for run in filtered_runs
            if run.get('path', '').endswith(workflow_name) or 
               run.get('name', '') == workflow_name
        ]
    
    # Filter fields if specified
    if fields:
        filtered_runs = _filter_fields(filtered_runs, fields)
    
    return filtered_runs


def get_workflow_run_details(
    repo_owner: str,
    repo_name: str,
    run_id: int,
    fields: Optional[List[str]] = None
) -> Optional[Dict[str, Any]]:
    """
    Get detailed information about a specific workflow run.
    
    Args:
        repo_owner: Repository owner (username or organization)
        repo_name: Repository name
        run_id: Workflow run ID
        fields: Optional list of field names to include in results
                Supports dot notation (e.g., ['id', 'name', 'actor.login'])
                If None, returns all fields
        
    Returns:
        Workflow run details dict, or None on error
        Contains: id, name, status, conclusion, created_at, updated_at, 
                  run_started_at, html_url, jobs_url, logs_url, timing_ms, etc.
        
    Example:
        >>> details = get_workflow_run_details('rbwatson', 'to-do-service-auto', 12345)
        >>> details['conclusion']
        'success'
        >>> details['run_duration_ms']
        125000
        
        >>> # Return only specific fields
        >>> details = get_workflow_run_details('rbwatson', 'to-do-service-auto', 12345,
        ...                                     fields=['id', 'conclusion', 'created_at'])
    """
    endpoint = f'/repos/{repo_owner}/{repo_name}/actions/runs/{run_id}'
    
    response = _run_gh_api(endpoint)
    if response is None:
        return None
    
    # Filter fields if specified
    if fields:
        response = _filter_fields(response, fields)
    
    return response


def list_workflow_jobs(
    repo_owner: str,
    repo_name: str,
    run_id: int,
    fields: Optional[List[str]] = None
) -> Optional[List[Dict[str, Any]]]:
    """
    List all jobs for a specific workflow run.
    
    Args:
        repo_owner: Repository owner (username or organization)
        repo_name: Repository name
        run_id: Workflow run ID
        fields: Optional list of field names to include in results
                Supports dot notation (e.g., ['id', 'name', 'runner.name'])
                If None, returns all fields
        
    Returns:
        List of job dictionaries, or None on error
        Each dict contains: id, name, status, conclusion, started_at, 
                           completed_at, steps, etc.
        
    Example:
        >>> jobs = list_workflow_jobs('rbwatson', 'to-do-service-auto', 12345)
        >>> len(jobs)
        4
        >>> jobs[0]['name']
        'Validate Testing Tools'
        
        >>> # Return only specific fields
        >>> jobs = list_workflow_jobs('rbwatson', 'to-do-service-auto', 12345,
        ...                           fields=['id', 'name', 'conclusion'])
    """
    endpoint = f'/repos/{repo_owner}/{repo_name}/actions/runs/{run_id}/jobs'
    
    params = {'per_page': '100'}
    
    response = _run_gh_api(endpoint, params)
    if response is None:
        return None
    
    jobs = response.get('jobs', [])
    
    # Filter fields if specified
    if fields:
        jobs = _filter_fields(jobs, fields)
    
    return jobs


def get_workflow_job_details(
    repo_owner: str,
    repo_name: str,
    job_id: int,
    fields: Optional[List[str]] = None
) -> Optional[Dict[str, Any]]:
    """
    Get detailed information about a specific workflow job.
    
    Args:
        repo_owner: Repository owner (username or organization)
        repo_name: Repository name
        job_id: Job ID
        fields: Optional list of field names to include in results
                Supports dot notation (e.g., ['id', 'name', 'steps.name'])
                If None, returns all fields
        
    Returns:
        Job details dict including all steps, or None on error
        Contains: id, name, status, conclusion, started_at, completed_at,
                 steps (with name, status, conclusion, number, started_at, 
                 completed_at for each step)
        
    Example:
        >>> job = get_workflow_job_details('rbwatson', 'to-do-service-auto', 67890)
        >>> job['name']
        'Lint Markdown Files'
        >>> len(job['steps'])
        8
        >>> job['steps'][0]['name']
        'Checkout code'
        
        >>> # Return only specific fields
        >>> job = get_workflow_job_details('rbwatson', 'to-do-service-auto', 67890,
        ...                                 fields=['id', 'name', 'conclusion'])
    """
    endpoint = f'/repos/{repo_owner}/{repo_name}/actions/jobs/{job_id}'
    
    response = _run_gh_api(endpoint)
    if response is None:
        return None
    
    # Filter fields if specified
    if fields:
        response = _filter_fields(response, fields)
    
    return response


def get_workflow_run_timing(
    repo_owner: str,
    repo_name: str,
    run_id: int
) -> Optional[Dict[str, Any]]:
    """
    Get timing information for a workflow run and its jobs.
    
    Args:
        repo_owner: Repository owner (username or organization)
        repo_name: Repository name
        run_id: Workflow run ID
        
    Returns:
        Dict with timing information, or None on error
        Contains:
        - run_duration_seconds: Total workflow duration
        - jobs: List of dicts with job name, duration_seconds, status
        - total_job_time_seconds: Sum of all job durations
        
    Example:
        >>> timing = get_workflow_run_timing('rbwatson', 'to-do-service-auto', 12345)
        >>> timing['run_duration_seconds']
        125.5
        >>> timing['jobs'][0]['name']
        'Validate Testing Tools'
        >>> timing['jobs'][0]['duration_seconds']
        45.2
    """
    run_details = get_workflow_run_details(repo_owner, repo_name, run_id)
    if run_details is None:
        return None
    
    jobs = list_workflow_jobs(repo_owner, repo_name, run_id)
    if jobs is None:
        return None
    
    # Calculate run duration
    run_started = run_details.get('run_started_at')
    run_updated = run_details.get('updated_at')
    
    run_duration = None
    if run_started and run_updated:
        start_time = datetime.fromisoformat(run_started.replace('Z', '+00:00'))
        end_time = datetime.fromisoformat(run_updated.replace('Z', '+00:00'))
        run_duration = (end_time - start_time).total_seconds()
    
    # Calculate job durations
    job_timings = []
    total_job_time = 0
    
    for job in jobs:
        started = job.get('started_at')
        completed = job.get('completed_at')
        
        duration = None
        if started and completed:
            start_time = datetime.fromisoformat(started.replace('Z', '+00:00'))
            end_time = datetime.fromisoformat(completed.replace('Z', '+00:00'))
            duration = (end_time - start_time).total_seconds()
            total_job_time += duration
        
        job_timings.append({
            'name': job.get('name'),
            'status': job.get('status'),
            'conclusion': job.get('conclusion'),
            'duration_seconds': duration
        })
    
    return {
        'run_duration_seconds': run_duration,
        'total_job_time_seconds': total_job_time,
        'jobs': job_timings
    }
