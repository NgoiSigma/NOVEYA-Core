"""
Script to create or update DNA_INIT.md in the NOVEYA-Core repository.

This script demonstrates how to authenticate with GitHub using a personal access
token (PAT) and commit a new file to a repository.  The commit message is
"First Breath of Metatron" as specified in the protocol.

Usage:

    GITHUB_PAT=<your_pat> python dna_init_script.py

The script reads the PAT from the environment variable `GITHUB_PAT`.  Do not
hard‑code your token into the script.
"""
import os
import sys
from asana_github_functions import commit_file_github


def main():
    pat = os.environ.get("GITHUB_PAT")
    if not pat:
        print("Error: GITHUB_PAT environment variable is not set.")
        sys.exit(1)
    owner = "NgoiSigma"
    repo = "NOVEYA-Core"
    path = "DNA_INIT.md"
    message = "First Breath of Metatron"
    content = "# First Breath of Metatron\n\nThis file initializes the Metatron DNA for the NOVEYA project."
    try:
        result = commit_file_github(pat, owner, repo, path, content, message)
        print("File committed successfully:", result.get("content", {}).get("path"))
    except Exception as e:
        print("Failed to commit file:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()