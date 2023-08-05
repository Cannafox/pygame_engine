import numpy as np
import pygame

class Renderer:
    def __init__(self, frame):
        self.frame = frame
    def render_frame(self):
        pass


class Pixel:
    def __init__(self, value=(0, 0, 0)):
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_color(self):
        return self.value

class Screen:
    def __init__(self, default_config = None):
        self.width = default_config['SIZE']['WIDTH']
        self.height = default_config['SIZE']['HEIGHT']
        self.canvas = np.empty((self.width, self.height), dtype=object)
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clear_canvas()
        print("Screen initialized")

    def clear_canvas(self):
        for x in range(self.width):
            for y in range(self.height):
                self.canvas[x, y] = Pixel()

    def get_size(self):
        return (self.width, self.height)

    def draw_rectangle(self, pos, width=50, height=50, filled=True):
        for x in range(pos[0]-width//2, pos[0]+width//2, 1):
            for y in range(pos[1]-height//2, pos[1]+height//2, 1):
                self.canvas[x % (self.width - 1), y % (self.height - 1)].set_value((255, 255, 255))
                pygame.draw.rect(self.window, pygame.Color(255, 255, 255), (x-5, y-5, 10, 10))

    def update(self, pos, value):
        self.canvas[pos].set_value(value)

    def randomize_screen(self):
        self.canvas = np.random.randint(0, 254, size=(self.width, self.height, 3))

    def draw(self):
        print(self.canvas)
        surface = pygame.surfarray.make_surface(self.canvas)
        self.window.blit(surface, (0,0))
        #for x in range(0, self.width):
        #   for y in range(0, self.height):
        #       color = self.canvas[x, y].get_color()



