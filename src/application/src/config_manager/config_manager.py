import os
import json

class ConfigManager:
    CONFIG = None

    def __init__(self, fn):
        print(fn)
        self.load_config(fn)

    @staticmethod
    def _parse_config_file(config):
        return config

    def load_config(self, fn=None):
        is_ok = False
        full_path = os.path.join(os.path.dirname(__file__), 'data', fn)
        assert os.path.isfile, f"Configuration file {full_path} not found!"

        print(f"Loading {full_path} configuration file...")
        with open(full_path, "r") as f:
            config = json.load(f)
        is_ok = True

        ConfigManager.CONFIG = self._parse_config_file(config)

        return is_ok

    @property
    def config(self):
        return ConfigManager.CONFIG
