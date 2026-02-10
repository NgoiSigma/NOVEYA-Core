"""
Simple linter to detect common sources of frequency noise in Python scripts.

This linter scans Python source files for patterns that are considered
"frequency noise" in the context of the NOVEYA project.  Frequency noise
includes unnecessary debug output, incomplete TODO markers, or usage of
forbidden modules.

To use this linter, run:

    python linter.py path/to/script.py

The script will exit with status 0 if no issues are found, or 1 if
potential noise is detected.  It prints a report of issues to stdout.
"""
import re
import sys
from pathlib import Path

NOISE_PATTERNS = [
    (re.compile(r"print\s*\("), "Direct print statements produce uncontrolled output. Use logging instead."),
    (re.compile(r"TODO"), "TODO markers indicate unfinished thoughts; resolve or remove them."),
    (re.compile(r"import\s+pdb"), "Do not include debugger imports in committed code."),
    (re.compile(r"time\.sleep\("), "Sleep calls can stall automation; evaluate necessity."),
]

def lint_file(path: Path) -> int:
    content = path.read_text(encoding="utf-8")
    issues = []
    for pattern, message in NOISE_PATTERNS:
        for match in pattern.finditer(content):
            line_no = content.count("\n", 0, match.start()) + 1
            issues.append((line_no, message, match.group(0)))
    if issues:
        print(f"Noise detected in {path}:")
        for line, message, snippet in issues:
            print(f"  Line {line}: {message} (found '{snippet}')")
        return 1
    else:
        print(f"No noise detected in {path}.")
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python linter.py <path_to_python_file>")
        sys.exit(2)
    file_path = Path(sys.argv[1])
    if not file_path.is_file():
        print(f"File not found: {file_path}")
        sys.exit(2)
    exit_code = lint_file(file_path)
    sys.exit(exit_code)