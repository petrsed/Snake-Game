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

    def update(self):

        self.set_image()
        self.rect.x = random.randrange(110, 890)
        self.rect.y = random.randrange(175, 790)

    def set_image(self):
        self.image = pygame.transform.scale(random.choice(self.images), self.size)
        self.rect = self.image.get_rect()

    def get_pos(self):
        return self.rect.x, self.rect.y

    def load_image(self, name):
        fullname = os.path.join('data/food/', name)
        image = pygame.image.load(fullname)
        return image
