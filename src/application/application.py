import os
import json
from .src.screen import screen
from .src.config_manager import config_manager

class Application:
    CONFIG = None
    def __init__(self, config_fn="config.json"):
        self.config_manager = config_manager.ConfigManager(config_fn)
        self.CONFIG = self.config_manager.config["APPLICATION"]

        self.screen = screen.Screen(self.CONFIG['SCREEN'])

    def run(self):
        self.screen.draw()

        return False





