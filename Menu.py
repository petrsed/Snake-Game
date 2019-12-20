import pygame
import sys
from Game import Game


class MainMenu:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.x, self.y = self.screen_size
        self.menu_screen = pygame.display.set_mode(screen_size)
        self.menu_background_image = pygame.image.load('data/menu_background.png').convert()
        self.clock = pygame.time.Clock()
        pygame.display.update()

    def start(self):
        self.menu_on = True
        while self.menu_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_click(event.pos)
            self.menu_screen.blit(self.menu_background_image, (0, 0))
            pygame.display.flip()
            self.clock.tick(60)

    def get_click(self, coords):
        x, y = coords
        if x >= 327 and x <= 674 and y >= 751 and y <= 849:
            menu = Game(self.screen_size)
            menu.start()

    def terminate(self):
        pygame.quit()
        sys.exit()


class PauseMenu:
    def __init__(self, size):
        self.screen_size = size
        self.x, self.y = self.screen_size
        self.menu_screen = pygame.display.set_mode(self.screen_size)
        self.menu_background_image = pygame.image.load('data/pause_background.png').convert()
        self.clock = pygame.time.Clock()
        pygame.display.update()

    def start(self):
        self.pause_on = True
        while self.pause_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_click(event.pos)
            self.menu_screen.blit(self.menu_background_image, (0, 0))
            pygame.display.flip()
            self.clock.tick(60)

    def get_click(self, coords):
        x, y = coords
        if x >= 282 and x <= 717 and y >= 438 and y <= 483:
            self.pause_on = False
        elif x >= 308 and x <= 692 and y >= 494 and y <= 537:
            new_game = Game(self.screen_size)
            new_game.start()
        elif x >= 399 and x <= 600 and y >= 549 and y <= 594:
            menu = MainMenu(self.screen_size)
            menu.start()

    def terminate(self):
        pygame.quit()
        sys.exit()
