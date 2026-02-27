"""Cross-platform way to start the service in development mode."""

import os

from app.main import start


if __name__ == "__main__":
    # Ensure selection of the development config without requiring shell-specific exports.
    os.environ["ENV"] = "dev"
    start()
