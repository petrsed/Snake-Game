import pygame
import random


class Wall(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load('data/obstacles/BricksWall.png')
        self.rect = None
        self.size = 50, 50
        self.screen_width, self.screen_height = screen_width, screen_height
        self.update()

    def spawn(self):
        self.set_image()
        self.rect.x = random.randrange(110, 890)
        self.rect.y = random.randrange(175, 790)

    def set_image(self):
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()

    def get_pos(self):
        return self.rect.x, self.rect.y

