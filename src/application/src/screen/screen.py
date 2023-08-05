class Screen:
    WIDTH = 0
    HEIGHT = 0
    PIXEL_DATA = None

    def __init__(self, default_config = None):
        self.load_config(default_config)
        print("Screen initialized")

    def load_config(self, default_config):
        self.WIDTH = default_config["SIZE"]["WIDTH"]
        self.HEIGHT = default_config["SIZE"]["HEIGHT"]

        print(f"Setting screen:\n  WIDTH = {self.WIDTH}\n  HEIGHT = {self.HEIGHT}")

    def draw(self):
        pass

