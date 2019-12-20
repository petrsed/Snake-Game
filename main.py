import pygame
import random


class Snake:
    right = 'RIGHT'
    left = 'LEFT'
    up = 'UP'
    down = 'DOWN'

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.snake_size = 20
        self.snake_step = 10
        self.snake_head_pos = [100, 50]
        self.snake_body_pos = [[90, 50], [80, 50]]
        self.direction = self.up
        self.change_direction = self.direction

    def check_direction(self):
        if (self.change_direction == self.right and not self.direction == self.left) or\
                (self.change_direction == self.left and not self.direction == self.right) or\
                (self.change_direction == self.up and not self.direction == self.down) or\
                (self.change_direction == self.down and not self.direction == self.up):
            self.direction = self.change_direction
            return True
        return False

    def change_head_pos(self):
        if not self.check_direction():
            return
        if self.direction == self.right:
            self.snake_head_pos[0] += self.snake_step
        elif self.direction == self.left:
            self.snake_head_pos[0] -= self.snake_step
        elif self.direction == self.up:
            self.snake_head_pos[1] -= self.snake_step
        elif self.direction == self.down:
            self.snake_head_pos[1] += self.snake_step

    def check_snake(self, score, food_pos):
        self.snake_body_pos.insert(0, self.snake_head_pos)
        if self.snake_head_pos == food_pos:
            score += 1
        else:
            self.snake_body_pos.pop()
        return score

    def draw_snake(self, surface, game):
        game.draw_map()  # Прорисовка карты
        for pos in self.snake_body_pos:
            pygame.draw.rect(surface, pygame.Color('blue'), pygame.Rect(*pos, self.snake_size, self.snake_size))

    def check_collision(self, game):
        if self.check_boundaries() or self.check_eating_oneself():
            game.game_over()  # game - экземпляр класса Game

    def check_boundaries(self):
        return (self.snake_head_pos[0] > self.screen_width or self.snake_head_pos[0] < 0)\
               or (self.snake_head_pos[1] > self.screen_height or self.snake_head_pos[1] < 0)

    def check_eating_oneself(self):
        for block in self.snake_body_pos:
            return block[0] == self.snake_head_pos[0] and block[1] == self.snake_head_pos[1]


class Food:
    def __init__(self, food_image, screen_width, screen_height):
        self.food_image = food_image
        self.food_size = 10
        self.food_pos = [random.randrange(1, screen_width // self.food_size) * self.food_size,
                         random.randrange(1, screen_height // self.food_size) * self.food_size]

    def draw_food(self, surface):
        x, y = self.food_pos
        pygame.draw.rect(surface, pygame.Color('red'), pygame.Rect(x, y, self.food_size, self.food_size))

    def set_food_pos(self, pos):
        self.food_pos = pos
