import os
import pygame
from .src.screen import screen

class Application:
    def __init__(self, config):
        self.config = config.get_application_config()
        self.screen = screen.Screen(config.get_screen_config())
        self.clock = pygame.time.Clock()
        self.running = False

    def run(self):
        self.running = True
        pygame.init()
        pos = None
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in {pygame.K_ESCAPE, pygame.K_q}:
                        self.running = False
                        break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = None

            if pos:
                self.screen.draw_rectangle(pos)
            self.screen.draw()
            pygame.display.flip()
            self.clock.tick(self.config["FPS"])
        pygame.quit()





