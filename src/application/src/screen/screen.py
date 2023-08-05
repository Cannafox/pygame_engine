import numpy as np
class Pixel:
    def __init__(self, value=0):
        self.value = value

    def get_pixel_color(self):
        return self.value

class Screen:
    def __init__(self, default_config = None):
        self.width = default_config['SIZE']['WIDTH']
        self.height = default_config['SIZE']['HEIGHT']
        self.canvas = np.empty((self.width, self.height), dtype=object)
        self.clear_canvas()
        print("Screen initialized")
        self.draw()

    def clear_canvas(self):
        for x in range(self.width):
            for y in range(self.height):
                self.canvas[x, y] = Pixel()

    def draw(self):
        for x in range(self.width):
            for y in range(in self.height):
                print(self.canvas[x, y].get_pixel_color())
            print("")


