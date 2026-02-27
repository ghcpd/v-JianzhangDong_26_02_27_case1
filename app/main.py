import os
import yaml
from .service import calculate_total

# load configuration based on the ENV variable

def load_config():
    env = os.environ.get('ENV','prod').lower()
    path = 'config.dev.yaml' if env=='dev' else 'config.yaml'
    with open(path,'r') as f:
        return yaml.safe_load(f)


def start():
    config = load_config()
    print('Service started in', config.get('env'))
