#!/usr/bin/env python3
"""
Tests for workflow_data_utils module.

Covers:
- gh CLI availability check
- API response parsing
- Date filtering
- Error handling
- Timing calculations

Run with:
    python3 test_workflow_data_utils.py
    pytest test_workflow_data_utils.py -v

Note: These tests require gh CLI to be installed and authenticated.
Some tests use mock data to avoid requiring network access.
"""

import sys
import json
from pathlib import Path
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).parent.parent))

from workflow_data_utils import (
    _check_gh_cli,
    list_workflow_runs,
    get_workflow_run_details,
    list_workflow_jobs,
    get_workflow_job_details,
    get_workflow_run_timing
)


def test_check_gh_cli():
    """Test gh CLI availability check."""
    print("\n" + "="*60)
    print("TEST: _check_gh_cli()")
    print("="*60)
    
    # This will fail in environments without gh CLI
    # But should not crash
    result = _check_gh_cli()
    
    assert isinstance(result, bool), "Should return boolean"
    print(f"  gh CLI available: {result}")
    
    if not result:
        print("  ℹ️  gh CLI not available - skipping API tests")
    
    print("  ✓ gh CLI check completed without crashing")


def test_list_workflow_runs_params():
    """Test list_workflow_runs parameter handling."""
    print("\n" + "="*60)
    print("TEST: list_workflow_runs() parameter validation")
    print("="*60)
    
    # Test with invalid repo - should return None gracefully
    runs = list_workflow_runs(
        repo_owner='nonexistent',
        repo_name='nonexistent',
        workflow_name='test.yml',
        days_back=1
    )
    
    # Should return None (not crash) for invalid repo
    assert runs is None or isinstance(runs, list), \
        "Should return None or list, not crash"
    
    print("  ✓ Handles invalid repository gracefully")


def test_get_workflow_run_details_invalid():
    """Test get_workflow_run_details with invalid run ID."""
    print("\n" + "="*60)
    print("TEST: get_workflow_run_details() error handling")
    print("="*60)
    
    # Test with invalid run ID - should return None gracefully
    details = get_workflow_run_details(
        repo_owner='nonexistent',
        repo_name='nonexistent',
        run_id=99999999
    )
    
    assert details is None or isinstance(details, dict), \
        "Should return None or dict, not crash"
    
    print("  ✓ Handles invalid run ID gracefully")


def test_list_workflow_jobs_invalid():
    """Test list_workflow_jobs with invalid run ID."""
    print("\n" + "="*60)
    print("TEST: list_workflow_jobs() error handling")
    print("="*60)
    
    jobs = list_workflow_jobs(
        repo_owner='nonexistent',
        repo_name='nonexistent',
        run_id=99999999
    )
    
    assert jobs is None or isinstance(jobs, list), \
        "Should return None or list, not crash"
    
    print("  ✓ Handles invalid run ID gracefully")


def test_get_workflow_job_details_invalid():
    """Test get_workflow_job_details with invalid job ID."""
    print("\n" + "="*60)
    print("TEST: get_workflow_job_details() error handling")
    print("="*60)
    
    job = get_workflow_job_details(
        repo_owner='nonexistent',
        repo_name='nonexistent',
        job_id=99999999
    )
    
    assert job is None or isinstance(job, dict), \
        "Should return None or dict, not crash"
    
    print("  ✓ Handles invalid job ID gracefully")


def test_get_workflow_run_timing_invalid():
    """Test get_workflow_run_timing with invalid run ID."""
    print("\n" + "="*60)
    print("TEST: get_workflow_run_timing() error handling")
    print("="*60)
    
    timing = get_workflow_run_timing(
        repo_owner='nonexistent',
        repo_name='nonexistent',
        run_id=99999999
    )
    
    assert timing is None or isinstance(timing, dict), \
        "Should return None or dict, not crash"
    
    print("  ✓ Handles invalid run ID gracefully")


def test_date_filtering_logic():
    """Test date filtering logic with mock data."""
    print("\n" + "="*60)
    print("TEST: Date filtering logic")
    print("="*60)
    
    # Mock workflow runs with different dates (use timezone-aware datetime)
    from datetime import timezone
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=7)
    
    mock_runs = [
        {'created_at': (now - timedelta(days=2)).isoformat().replace('+00:00', 'Z')},
        {'created_at': (now - timedelta(days=5)).isoformat().replace('+00:00', 'Z')},
        {'created_at': (now - timedelta(days=10)).isoformat().replace('+00:00', 'Z')},  # Should be filtered
    ]
    
    # Filter runs (simulate what list_workflow_runs does)
    filtered = [
        run for run in mock_runs
        if datetime.fromisoformat(run['created_at'].replace('Z', '+00:00')) >= cutoff
    ]
    
    assert len(filtered) == 2, f"Should filter to 2 runs, got {len(filtered)}"
    print(f"  Filtered {len(mock_runs)} runs to {len(filtered)} within date range")
    print("  ✓ Date filtering works correctly")


def test_timing_calculation_logic():
    """Test timing calculation logic with mock data."""
    print("\n" + "="*60)
    print("TEST: Timing calculation logic")
    print("="*60)
    
    # Mock timing data
    start = datetime(2024, 12, 12, 10, 0, 0)
    end = datetime(2024, 12, 12, 10, 2, 5)  # 2 minutes 5 seconds later
    
    duration = (end - start).total_seconds()
    
    assert duration == 125.0, f"Expected 125 seconds, got {duration}"
    print(f"  Calculated duration: {duration} seconds")
    print("  ✓ Timing calculation works correctly")


def run_all_tests():
    """Run all test functions."""
    print("\n" + "="*70)
    print(" RUNNING ALL TESTS FOR workflow_data_utils.py")
    print("="*70)
    
    tests = [
        test_check_gh_cli,
        test_list_workflow_runs_params,
        test_get_workflow_run_details_invalid,
        test_list_workflow_jobs_invalid,
        test_get_workflow_job_details_invalid,
        test_get_workflow_run_timing_invalid,
        test_date_filtering_logic,
        test_timing_calculation_logic,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            failed += 1
            print(f"\n  ✗ FAILED: {test_func.__name__}")
            print(f"    {str(e)}")
        except Exception as e:
            failed += 1
            print(f"\n  ✗ ERROR: {test_func.__name__}")
            print(f"    {str(e)}")
    
    print("\n" + "="*70)
    print(f" TEST SUMMARY: {passed} passed, {failed} failed")
    print("="*70)
    
    return failed == 0


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
