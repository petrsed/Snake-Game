import pygame


class SoundButton(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.mode = True
        self.on_image = pygame.image.load('data/buttons/SoundOn.png')
        self.off_image = pygame.image.load('data/buttons/SoundOff.png')
        self.screen = screen

    def switch_music(self):
        self.mode = not self.mode
        if not self.mode:
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.play(1)

    def draw(self):
        if self.mode:
            image = self.on_image
        else:
            image = self.off_image
        self.screen.blit(image, (930, 10))

    def check_mode(self):
        return self.mode
