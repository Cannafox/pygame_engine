import os
from .src.screen import screen

class Application:
    def __init__(self, config):
        self.config = config.get_application_config()
        self.screen = screen.Screen(config.get_screen_config())





