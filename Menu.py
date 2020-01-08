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
        if x >= 285 and x <= 714 and y >= 392 and y <= 434:
            self.pause_on = False
        elif x >= 308 and x <= 692 and y >= 449 and y <= 491:
            new_game = Game(self.screen_size)
            new_game.start()
        elif x >= 399 and x <= 600 and y >= 503 and y <= 544:
            menu = MainMenu(self.screen_size)
            menu.start()
        elif x >= 263 and x <= 755 and y >= 552 and y <= 598:
            self.terminate()

    def terminate(self):
        pygame.quit()
        sys.exit()


class LoseMenu:
    def __init__(self, size):
        self.screen_size = size
        self.x, self.y = self.screen_size
        self.menu_screen = pygame.display.set_mode(self.screen_size)
        self.menu_background_image = pygame.image.load('data/lose_background.png').convert()
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
        if x >= 304 and x <= 690 and y >= 431 and y <= 470:
            new_game = Game(self.screen_size)
            new_game.start()
        elif x >= 402 and x <= 601 and y >= 486 and y <= 529:
            menu = MainMenu(self.screen_size)
            menu.start()
        elif x >= 254 and x <= 748 and y >= 541 and y <= 582:
            self.terminate()

    def terminate(self):
        pygame.quit()
        sys.exit()
