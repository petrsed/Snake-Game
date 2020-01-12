import pygame
import random
import os
from random import choice


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


class Snake:
    right = 'RIGHT'
    left = 'LEFT'
    up = 'UP'
    down = 'DOWN'

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.snake_size = 20
        self.snake_step = 20
        self.snake_head_pos = [100, 300]
        self.snake_body_pos = [[value, 300] for value in range(150, 0, -30)]
        self.direction = self.right

    def check_direction(self, change_direction):
        if (change_direction == self.right and not self.direction == self.left) or\
                (change_direction == self.left and not self.direction == self.right) or\
                (change_direction == self.up and not self.direction == self.down) or\
                (change_direction == self.down and not self.direction == self.up):
            self.direction = change_direction
            return True
        return False

    def change_head_pos(self):
        if self.direction == self.right:
            self.snake_head_pos[0] += self.snake_step
        elif self.direction == self.left:
            self.snake_head_pos[0] -= self.snake_step
        elif self.direction == self.up:
            self.snake_head_pos[1] -= self.snake_step
        elif self.direction == self.down:
            self.snake_head_pos[1] += self.snake_step

    def check_snake(self, food_pos, food_size):
        self.snake_body_pos.insert(0, list(self.snake_head_pos))
        x_snake_1, y_snake_1 = self.snake_head_pos
        x_snake_2, y_snake_2 = x_snake_1 + self.snake_size, y_snake_1 + self.snake_size
        x_food_1, y_food_1 = food_pos
        x_food_2, y_food_2 = x_food_1 + food_size, y_food_1 + food_size
        if x_food_1 <= x_snake_2 <= x_food_2 and y_food_1 <= y_snake_2 <= y_food_2:
            return True
        self.snake_body_pos.pop()
        return False

    def draw_snake(self, surface):
        for pos in self.snake_body_pos:
            surface.fill(pygame.Color('blue'), pygame.Rect(pos, (self.snake_size, self.snake_size)))

    def check_collision(self, game):
        if self.check_boundaries() or self.check_eating_oneself():
            game.game_over()

    def check_boundaries(self):
        return (self.snake_head_pos[0] > 920 or self.snake_head_pos[0] < 60)\
               or (self.snake_head_pos[1] > 830 or self.snake_head_pos[1] < 105)

    def check_eating_oneself(self):
        for block in self.snake_body_pos[1:]:
            return block[0] == self.snake_head_pos[0] and block[1] == self.snake_head_pos[1]


class Food(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.images = [load_image(el) for el in ['apple.png', 'banana.png', 'cherry.png']]
        self.image = None
        self.rect = None
        self.size = 50, 50
        self.screen_width, self.screen_height = screen_width, screen_height
        self.update()

    def update(self):
        self.set_image()
        self.rect.x = random.randrange(110, 890)
        self.rect.y = random.randrange(175, 790)

    def set_image(self):
        self.image = pygame.transform.scale(choice(self.images), self.size)
        self.rect = self.image.get_rect()

    def get_pos(self):
        return self.rect.x, self.rect.y


