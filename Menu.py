import pygame
import sys
from Game import SoloGame, DuoGame


class StartMenu:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.x, self.y = self.screen_size
        self.menu_screen = pygame.display.set_mode(screen_size)
        self.menu_background_image = pygame.image.load('data/backgrounds/StartMenuBackground.png').convert()
        self.clock = pygame.time.Clock()
        pygame.display.update()
        pygame.mixer.music.load('data/music/logo.mp3')

    def start(self):
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(0.4)
        self.menu_on = True
        while self.menu_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_click(event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game = SoloGame(self.screen_size)
                        game.start()
            self.menu_screen.blit(self.menu_background_image, (0, 0))
            pygame.display.flip()
            self.clock.tick(60)

    def get_click(self, coords):
        x, y = coords
        if x >= 430 and x <= 620 and y >= 641 and y <= 696:
            game = DuoGame(self.screen_size)
            game.start()
        elif x >= 346 and x <= 704 and y >= 720 and y <= 864:
            game = SoloGame(self.screen_size)
            game.start()
        elif x >= 0 and x <= 65 and y >= 0 and y <= 65:
            self.terminate()

    def terminate(self):
        pygame.quit()
        sys.exit()


class PauseMenu:
    def __init__(self, size, game_type):
        self.screen_size = size
        self.menu_screen = pygame.display.set_mode(self.screen_size)
        self.menu_background_image = pygame.image.load('data/backgrounds/PauseMenuBackground.png').convert()
        self.clock = pygame.time.Clock()
        self.game_type = game_type
        pygame.display.update()

    def start(self):
        self.pause_on = True
        while self.pause_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_click(event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause_on = False
                    if event.key == pygame.K_RETURN:
                        self.pause_on = False
            self.menu_screen.blit(self.menu_background_image, (0, 0))
            pygame.display.flip()
            self.clock.tick(60)

    def get_click(self, coords):
        x, y = coords
        if x >= 285 and x <= 714 and y >= 392 and y <= 434:
            self.pause_on = False
        elif x >= 308 and x <= 692 and y >= 449 and y <= 491:
            if self.game_type == 1:
                new_game = SoloGame(self.screen_size)
                new_game.start()
            elif self.game_type == 2:
                new_game = DuoGame(self.screen_size)
                new_game.start()
        elif x >= 399 and x <= 600 and y >= 503 and y <= 544:
            menu = StartMenu(self.screen_size)
            menu.start()
        elif x >= 263 and x <= 755 and y >= 552 and y <= 598:
            self.terminate()

    def terminate(self):
        pygame.quit()
        sys.exit()


class LoseMenu:
    def __init__(self, size, game_type):
        self.game_type = game_type
        self.screen_size = size
        self.menu_screen = pygame.display.set_mode(self.screen_size)
        self.menu_background_image = pygame.image.load('data/backgrounds/LoseMenuBackground.png').convert()
        self.clock = pygame.time.Clock()
        self.lose_sound = pygame.mixer.Sound('data/music/lose.wav')
        pygame.display.update()

    def start(self):
        pygame.mixer.Sound.play(self.lose_sound)
        self.menu_on = True
        while self.menu_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_click(event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = StartMenu(self.screen_size)
                        menu.start()
                    if event.key == pygame.K_RETURN:
                        if self.game_type == 2:
                            new_game = DuoGame(self.screen_size)
                            new_game.start()
                        elif self.game_type == 1:
                            new_game = SoloGame(self.screen_size)
                            new_game.start()
            self.menu_screen.blit(self.menu_background_image, (0, 0))
            pygame.display.flip()
            self.clock.tick(60)

    def get_click(self, coords):
        x, y = coords
        if x >= 304 and x <= 690 and y >= 431 and y <= 470:
            if self.game_type == 2:
                new_game = DuoGame(self.screen_size)
                new_game.start()
            elif self.game_type == 1:
                new_game = SoloGame(self.screen_size)
                new_game.start()
        elif x >= 402 and x <= 601 and y >= 486 and y <= 529:
            menu = StartMenu(self.screen_size)
            menu.start()
        elif x >= 254 and x <= 748 and y >= 541 and y <= 582:
            self.terminate()

    def terminate(self):
        pygame.quit()
        sys.exit()
