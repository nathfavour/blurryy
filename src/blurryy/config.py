import json
import os

DEFAULT_CONFIG = {
    "save_temp": False,
    "blur_value": 10 
}

def load_config():
    config_path = os.path.expanduser("~/.blurryyconfig.json")
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            user_config = json.load(f)
        config = {**DEFAULT_CONFIG, **user_config}
    else:
        config = DEFAULT_CONFIG
    return config
