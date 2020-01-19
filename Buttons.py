import pygame

class SoundOn(pygame.sprite.Sprite):
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