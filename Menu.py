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
        self.pause_on = False
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
        if 285 <= x <= 714 and 392 <= y <= 434:
            self.pause_on = False
        elif 308 <= x <= 692 and 449 <= y <= 491:
            if self.game_type == 1:
                new_game = SoloGame(self.screen_size)
                new_game.start()
            elif self.game_type == 2:
                new_game = DuoGame(self.screen_size)
                new_game.start()
        elif 399 <= x <= 600 and 503 <= y <= 544:
            menu = StartMenu(self.screen_size)
            menu.start()
        elif 263 <= x <= 755 and 552 <= y <= 598:
            self.terminate()

    def terminate(self):
        pygame.quit()
        sys.exit()


class LoseMenu:
    def __init__(self, size, game_type, first_score, second_score):
        self.game_type = game_type
        self.first_score = first_score
        self.second_score = second_score
        self.screen_size = size
        self.menu_screen = pygame.display.set_mode(self.screen_size)
        self.menu_background_image = pygame.image.load('data/backgrounds/LoseMenuBackground.png').convert()
        self.clock = pygame.time.Clock()
        self.lose_sound = pygame.mixer.Sound('data/music/lose.wav')
        self.first_snake_head = pygame.transform.scale(pygame.image.load('data/snake/red/SnakeHeadUp.png'), (50, 50))
        self.second_snake_head = pygame.transform.scale(pygame.image.load('data/snake/purple/SnakeHeadUp.png'), (50, 50))
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
            if self.second_score != -1:
                self.show_score()
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

    def show_score(self):
        score_font = pygame.font.SysFont('tahoma', 50)
        first_score_surf = score_font.render('Score: {0}'.format(self.first_score), True, pygame.Color(255, 255, 255))
        second_score_surf = score_font.render('Score: {0}'.format(self.second_score), True, pygame.Color(255, 255, 255))

        first_score_rect = first_score_surf.get_rect()
        first_score_rect.midtop = (380, 255)
        second_score_rect = second_score_surf.get_rect()
        second_score_rect.midtop = (660, 255)

        self.menu_screen.blit(self.first_snake_head, (230, 263))
        self.menu_screen.blit(self.second_snake_head, (510, 263))
        self.menu_screen.blit(first_score_surf, first_score_rect)
        self.menu_screen.blit(second_score_surf, second_score_rect)

    def terminate(self):
        pygame.quit()
        sys.exit()
