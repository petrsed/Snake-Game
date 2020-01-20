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

    def spawn(self, coords):
        self.set_image()
        x_values = set(range(110, 890))
        y_values = set(range(175, 790))
        for x_coord, y_coord in coords:
            x_values -= set(range(x_coord - self.size[0] // 2, x_coord + int(self.size[0] * 1.5) + 1))
            y_values -= set(range(y_coord - self.size[0] // 2, y_coord + int(self.size[0] * 1.5) + 1))
        self.rect.x = random.choice(list(x_values))
        self.rect.y = random.choice(list(y_values))

    def set_image(self):
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()

    def get_pos(self):
        return self.rect.x, self.rect.y

