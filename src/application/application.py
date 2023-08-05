import os
import json
from .src.screen import screen
from .src.config_manager import config_manager

class Application:
    def __init__(self, config_fn = "config.json"):
        self.config_manager = config_manager.ConfigManger(config_fn)

        self.screen = screen.Screen()





