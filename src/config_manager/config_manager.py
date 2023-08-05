import os
import json

class ConfigManager:
    def __init__(self, file_path=None):
        self.default_config_path = os.path.join("data", "config.json")
        self.configs = {}
        if file_path:
            print(f"Loading given config file {file_path}...")
        else:
            file_path = os.path.join(os.path.dirname(__file__), self.default_config_path)
            print(f"Config file not specified, loading default configuration file {file_path}")
        self.load_config_file(file_path)
    def get_screen_config(self):
        return self.configs['SCREEN']

    def get_application_title(self):
        return self.configs['GENERAL']['TITLE']

    def get_application_fps(self):
        return self.configs['GENERAL']['FPS']

    def get_application_config(self):
        return self.configs['GENERAL']

    def load_config_file(self, file_path=None):
        assert os.path.isfile(file_path), f"Configuration file {file_path} not found!"

        print(f"Loading {file_path} configuration file...")
        with open(file_path, "r") as f:
            configs = json.load(f)

        self.configs = configs
