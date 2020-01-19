import pygame
import sys
import Menu
import Snake
import Food
import Obstacles
import os


class SoloGame:
    def __init__(self, screen_size):
        self.score = 0
        self.screen_size = screen_size
        self.x, self.y = self.screen_size
        self.menu_screen = pygame.display.set_mode(screen_size)
        self.menu_background_image = pygame.image.load('data/backgrounds/GameBackground.png').convert()
        self.clock = pygame.time.Clock()
        self.fps = 15
        self.next_wall_score_spawn = 10
        self.walls = list()
        self.level = 1
        pygame.display.update()

    def start(self):
        count = 0
        snake = Snake.Snake(self.x, self.y, 'red')
        food = Food.Food(self.x, self.y)
        pygame.mixer.music.load('data/music/soundtrack.mp3')
        self.food_sound = pygame.mixer.Sound('data/music/food.wav')
        self.level_up_sound = pygame.mixer.Sound('data/music/level.wav')
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(0.4)
        self.game_on = True
        while self.game_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        snake.check_direction("RIGHT")
                    elif event.key == pygame.K_LEFT or event.key == ord('a'):
                        snake.check_direction("LEFT")
                    elif event.key == pygame.K_UP or event.key == ord('w'):
                        snake.check_direction("UP")
                    elif event.key == pygame.K_DOWN or event.key == ord('s'):
                        snake.check_direction("DOWN")
                    elif event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.pause()
                        menu = Menu.PauseMenu(self.screen_size, 1)
                        menu.start()
                        pygame.mixer.music.unpause()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_click(event.pos)
            self.menu_screen.blit(self.menu_background_image, (0, 0))
            snake.change_head_pos()
            # for wall in self.walls:
            #    value = snake.check_snake(wall.get_pos(), wall.size[0])
            #    if value:
            #        self.game_over()
            value = snake.check_snake(food.get_pos(), food.size[0])
            if value:
                self.score += 1
                pygame.mixer.Sound.play(self.food_sound)
                snake.add_element_snake()
                food.update()

            if self.score == self.next_wall_score_spawn:
                wall = Obstacles.Wall(self.x, self.y)
                wall.spawn()
                self.level += 1
                pygame.mixer.Sound.play(self.level_up_sound)
                self.walls.append(wall)
                self.next_wall_score_spawn += 10
            for wall in self.walls:
                self.menu_screen.blit(wall.image, wall.rect)
            snake.snake_design()

            snake.update(self.menu_screen)
            snake.check_collision(self)
            self.menu_screen.blit(food.image, food.rect)
            self.show_score()
            self.show_level()
            pygame.display.flip()
            self.clock.tick(self.fps)
            count += 1
            self.show_score()

    def get_click(self, coords):
        x, y = coords
        if x <= 65 and y <= 65:
            pygame.mixer.music.pause()
            menu = Menu.PauseMenu(self.screen_size, 1)
            menu.start()
            pygame.mixer.music.unpause()

    def show_score(self):
        score_font = pygame.font.SysFont('tahoma', 50)
        score_surf = score_font.render('Score: {0}'.format(self.score), True, pygame.Color(255, 255, 255))
        score_rect = score_surf.get_rect()
        score_rect.midtop = (193, 5)
        self.menu_screen.blit(score_surf, score_rect)

    def show_level(self):
        score_font = pygame.font.SysFont('tahoma', 50)
        score_surf = score_font.render('Level: {0}'.format(self.level), True, pygame.Color(255, 255, 255))
        score_rect = score_surf.get_rect()
        score_rect.midtop = (500, 5)
        self.menu_screen.blit(score_surf, score_rect)

    def game_over(self):
        pygame.mixer.music.stop()
        lose_menu = Menu.LoseMenu(self.screen_size, 1)
        lose_menu.start()

    def terminate(self):
        pygame.quit()
        sys.exit()


class DuoGame:
    def __init__(self, screen_size):
        self.first_score, self.second_score = 0, 0
        self.screen_size = screen_size
        self.x, self.y = self.screen_size
        self.menu_screen = pygame.display.set_mode(screen_size)
        self.menu_background_image = pygame.image.load('data/backgrounds/GameBackground.png').convert()
        self.clock = pygame.time.Clock()
        self.fps = 15
        self.next_wall_score_spawn = 10
        self.walls = list()
        self.level = 1
        self.first_snake_head = pygame.transform.scale(pygame.image.load('data/snake/red/SnakeHeadUp.png'), (50, 50))
        self.second_snake_head = pygame.transform.scale(pygame.image.load('data/snake/purple/SnakeHeadUp.png'), (50, 50))
        pygame.mixer.music.load('data/music/soundtrack.mp3')
        self.food_sound = pygame.mixer.Sound('data/music/food.wav')
        self.level_up_sound = pygame.mixer.Sound('data/music/level.wav')
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(0.4)
        pygame.display.update()

    def start(self):
        count = 0
        first_snake, second_snake = Snake.Snake(self.x, self.y, 'red'), Snake.Snake(self.x, self.y, 'purple')
        food = Food.Food(self.x, self.y)
        game_on = True
        while game_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        first_snake.check_direction("RIGHT")
                    elif event.key == pygame.K_LEFT:
                        first_snake.check_direction("LEFT")
                    elif event.key == pygame.K_UP:
                        first_snake.check_direction("UP")
                    elif event.key == pygame.K_DOWN:
                        first_snake.check_direction("DOWN")
                    if event.key == ord('d'):
                        second_snake.check_direction("RIGHT")
                    elif event.key == ord('a'):
                        second_snake.check_direction("LEFT")
                    elif event.key == ord('w'):
                        second_snake.check_direction("UP")
                    elif event.key == ord('s'):
                        second_snake.check_direction("DOWN")
                    elif event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.pause()
                        menu = Menu.PauseMenu(self.screen_size, 2)
                        menu.start()
                        pygame.mixer.music.unpause()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_click(event.pos)
            self.menu_screen.blit(self.menu_background_image, (0, 0))
            first_snake.change_head_pos()
            second_snake.change_head_pos()
            # for wall in self.walls:
            #    value = snake.check_snake(wall.get_pos(), wall.size[0])
            #    if value:
            #        self.game_over()
            value = first_snake.check_snake(food.get_pos(), food.size[0])
            if value:
                self.first_score += 1
                pygame.mixer.Sound.play(self.food_sound)
                first_snake.add_element_snake()
                food.update()
            value = second_snake.check_snake(food.get_pos(), food.size[0])
            if value:
                self.second_score += 1
                pygame.mixer.Sound.play(self.food_sound)
                second_snake.add_element_snake()
                food.update()
            if (self.first_score + self.second_score) == self.next_wall_score_spawn:
                wall = Obstacles.Wall(self.x, self.y)
                wall.spawn()
                self.level += 1
                pygame.mixer.Sound.play(self.level_up_sound)
                self.walls.append(wall)
                self.next_wall_score_spawn += 10
            for wall in self.walls:
                self.menu_screen.blit(wall.image, wall.rect)
            first_snake.snake_design()
            second_snake.snake_design()

            first_snake.update(self.menu_screen)
            second_snake.update(self.menu_screen)
            first_snake.check_collision(self)
            second_snake.check_collision(self)

            self.menu_screen.blit(food.image, food.rect)
            self.show_score()
            self.show_level()
            pygame.display.flip()
            self.clock.tick(self.fps)
            count += 1
            self.show_score()

    def get_click(self, coords):
        x, y = coords
        if x <= 65 and y <= 65:
            pygame.mixer.music.pause()
            menu = Menu.PauseMenu(self.screen_size, 2)
            menu.start()
            pygame.mixer.music.unpause()

    def show_score(self):
        score_font = pygame.font.SysFont('tahoma', 50)
        first_score_surf = score_font.render('Score: {0}'.format(self.first_score), True, pygame.Color(255, 255, 255))
        second_score_surf = score_font.render('Score: {0}'.format(self.second_score), True, pygame.Color(255, 255, 255))

        first_score_rect = first_score_surf.get_rect()
        first_score_rect.midtop = (250, 5)
        second_score_rect = second_score_surf.get_rect()
        second_score_rect.midtop = (530, 5)

        self.menu_screen.blit(self.first_snake_head, (100, 13))
        self.menu_screen.blit(self.second_snake_head, (380, 13))
        self.menu_screen.blit(first_score_surf, first_score_rect)
        self.menu_screen.blit(second_score_surf, second_score_rect)

    def show_level(self):
        score_font = pygame.font.SysFont('tahoma', 50)
        score_surf = score_font.render('Level: {0}'.format(self.level), True, pygame.Color(255, 255, 255))
        score_rect = score_surf.get_rect()
        score_rect.midtop = (800, 5)
        self.menu_screen.blit(score_surf, score_rect)

    def game_over(self):
        pygame.mixer.music.stop()
        lose_menu = Menu.LoseMenu(self.screen_size, 2)
        lose_menu.start()

    def terminate(self):
        pygame.quit()
        sys.exit()
