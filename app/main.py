import os
import yaml
from .service import calculate_total


def start(config_path: str | None = None):
    # Choose config based on explicit path, then environment, then default.
    if config_path is None:
        env = os.environ.get("ENV", "prod")
        config_path = "config.dev.yaml" if env == "dev" else "config.yaml"

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    print("Service started in", config["env"])