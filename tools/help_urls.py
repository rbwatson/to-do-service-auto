#!/usr/bin/env python3
"""
Help documentation URLs for error messages and user guidance.

This module centralizes all help URLs used across the documentation testing tools.
Update URLs here to change them throughout all tools and workflows.
"""

# Base wiki URL
WIKI_BASE_URL = "https://github.com/UWC2-APIDOC/to-do-service-auto/wiki"

# Help page URLs
HELP_URLS = {
    # File and directory requirements
    'file_locations': f"{WIKI_BASE_URL}/File-Locations",
    
    # Git and commit guidelines
    'squashing_commits': f"{WIKI_BASE_URL}/Squashing-Commits",
    'merge_commits': f"{WIKI_BASE_URL}/Avoiding-Merge-Commits",
    'branch_update': f"{WIKI_BASE_URL}/Updating-Your-Branch",
    
    # Documentation format requirements
    'example_format': f"{WIKI_BASE_URL}/Example-Format",
    'front_matter': f"{WIKI_BASE_URL}/Frontmatter-Format",
}

# For backward compatibility - direct access to individual URLs
FILE_LOCATIONS_URL = HELP_URLS['file_locations']
SQUASHING_COMMITS_URL = HELP_URLS['squashing_commits']
MERGE_COMMITS_URL = HELP_URLS['merge_commits']
BRANCH_UPDATE_URL = HELP_URLS['branch_update']
EXAMPLE_FORMAT_URL = HELP_URLS['example_format']
FRONT_MATTER_URL = HELP_URLS['front_matter']
# End of help_urls.py