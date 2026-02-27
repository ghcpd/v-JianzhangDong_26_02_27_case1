import yaml
from .service import calculate_total


def start():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    print("Service started in", config["env"])