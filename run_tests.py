"""Utility to run pytest and store results.

This script is cross-platform and will create a ``logs/`` directory if it
doesn't already exist.  The JUnit XML output can be consumed by CI systems
or examined locally.
"""

import os
import subprocess


def main():
    os.makedirs("logs", exist_ok=True)
    # pytest will run from the workspace root so that imports work correctly
    result = subprocess.run(["python", "-m", "pytest", "--junitxml=logs/results.xml"], check=False)
    if result.returncode != 0:
        print("Some tests failed; see logs/results.xml for details.")
    else:
        print("All tests passed; results stored in logs/results.xml.")


if __name__ == "__main__":
    main()
