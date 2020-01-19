import pygame
import os



def load_image(name, snake_type):
    if snake_type == 'red':
        fullname = os.path.join('data/snake/red/', name)
    elif snake_type == 'purple':
        fullname = os.path.join('data/snake/purple/', name)
    image = pygame.image.load(fullname)
    return image


class Snake:
    right = 'RIGHT'
    left = 'LEFT'
    up = 'UP'
    down = 'DOWN'

    def __init__(self, screen_width, screen_height, snake_type):
        self.snake_type = snake_type
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.snake_size = 20
        self.snake_step = 20
        self.snake_head_pos = [100, 300]
        self.snake_body_pos = [[value, 300] for value in range(60, 0, -20)]
        self.turns = {}
        self.snake_sprites = [None] * 3
        self.direction = self.right

    def snake_design(self):
        for i in range(len(self.snake_body_pos)):
            element = self.snake_body_pos[i]
            if i == 0:
                self.snake_sprites[i] = SnakeHead(element, self.direction, self.snake_type)
            else:
                self.snake_sprites[i] = SnakeBody1(element, self.snake_type) if i % 2 == 0 else SnakeBody2(element, self.snake_type)

    def add_element_snake(self):
        self.snake_sprites.append(None)

    def update(self, surface):
        for el in self.snake_sprites:
            surface.blit(el.image, el.rect)

    def check_direction(self, change_direction):
        if (change_direction == self.right and not self.direction == self.left) or \
                (change_direction == self.left and not self.direction == self.right) or \
                (change_direction == self.up and not self.direction == self.down) or \
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
        x_snake, y_snake = self.snake_head_pos
        if self.direction == self.right:
            x_snake += self.snake_size
        elif self.direction == self.left:
            x_snake -= self.snake_size
        elif self.direction == self.up:
            y_snake -= self.snake_size
        elif self.direction == self.down:
            y_snake += self.snake_size
        x_food_1, y_food_1 = food_pos
        x_food_2, y_food_2 = x_food_1 + food_size, y_food_1 + food_size
        if x_food_1 < x_snake < x_food_2 and y_food_1 < y_snake < y_food_2:
            return True
        self.snake_body_pos.pop()
        return False

    def check_collision(self, game):
        if self.check_boundaries() or self.check_eating_oneself():
            game.game_over()

    def check_boundaries(self):
        return (self.snake_head_pos[0] > 920 or self.snake_head_pos[0] < 60) \
               or (self.snake_head_pos[1] > 830 or self.snake_head_pos[1] < 105)

    def check_eating_oneself(self):
        for x_body, y_body in self.snake_body_pos[1:]:
            if x_body == self.snake_head_pos[0] and y_body == self.snake_head_pos[1]:
                return True
        return False


class SnakeHead(pygame.sprite.Sprite):
    paths = {'RIGHT': 'SnakeHeadRight.png', 'LEFT': 'SnakeHeadLeft.png', 'UP': 'SnakeHeadUp.png',
             'DOWN': 'SnakeHeadDown.png'}

    def __init__(self, pos, direction, snake_type):
        super().__init__()
        self.image = pygame.transform.scale(load_image(self.paths[direction], snake_type), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.rect.x -= 20
        self.rect.y -= 20

    def get_pos(self):
        return self.rect.x, self.rect.y


class SnakeBody1(pygame.sprite.Sprite):
    def __init__(self, pos, snake_type):
        super().__init__()
        self.image = pygame.transform.scale(load_image("SnakeBody1.png", snake_type), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def get_pos(self):
        return self.rect.x, self.rect.y


class SnakeBody2(pygame.sprite.Sprite):
    def __init__(self, pos, snake_type):
        super().__init__()
        self.image = pygame.transform.scale(load_image("SnakeBody2.png", snake_type), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def get_pos(self):
        return self.rect.x, self.rect.y
