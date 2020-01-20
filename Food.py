import os
import pygame
import random


class Food(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.images = [self.load_image(el) for el in ['Apple.png', 'Banana.png', 'Cherry.png', 'Orange.png']]
        self.image = None
        self.rect = None
        self.size = 50, 50
        self.screen_width, self.screen_height = screen_width, screen_height

        self.update()

    def update(self, coords=[]):
        self.set_image()
        x_values = set(range(110, 890))
        y_values = set(range(175, 790))
        for x_coord, y_coord in coords:
            x_values -= set(range(x_coord - self.size[0] // 2, x_coord + int(self.size[0] * 1.5) + 1))
            y_values -= set(range(y_coord - self.size[0] // 2, y_coord + int(self.size[0] * 1.5) + 1))
        self.rect.x = random.choice(list(x_values))
        self.rect.y = random.choice(list(y_values))

    def set_image(self):
        self.image = pygame.transform.scale(random.choice(self.images), self.size)
        self.rect = self.image.get_rect()

    def get_pos(self):
        return self.rect.x, self.rect.y

    def load_image(self, name):
        fullname = os.path.join('data/food/', name)
        image = pygame.image.load(fullname)
        return image
