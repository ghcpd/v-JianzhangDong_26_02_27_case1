import argparse
import os

from app.main import start


def _parse_args():
    parser = argparse.ArgumentParser(description="Start the order analytics service")
    parser.add_argument("--env", choices=["dev", "prod"], help="Environment to run in (overrides ENV)")
    parser.add_argument("--config", help="Explicit path to a YAML config file")
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    if args.env:
        os.environ["ENV"] = args.env
    start(config_path=args.config)