import pygame

pygame.init()
screen_size = (1000, 800)
clock = pygame.time.Clock()


class Menu:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.x, self.y = self.screen_size
        self.menu_screen = pygame.display.set_mode(screen_size)
        self.menu_background_image = pygame.image.load('data/menu_background.png').convert()
        self.clock = pygame.time.Clock()
        pygame.display.update()

    def start(self):
        self.menu_on, self.game_on = True, True
        while self.menu_on:
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_on = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_click(event.pos)
            self.menu_screen.blit(self.menu_background_image, (0, 0))
            pygame.display.flip()
            self.clock.tick(60)

    def get_click(self, coords):
        x, y = coords
        if x >= 352 and x <= 648 and y >= 667 and y >= 667 and y <= 752:
            self.menu_on = False


menu = Menu(screen_size)
menu.start()

game_screen = pygame.display.set_mode(screen_size)
game_background_image = pygame.image.load('data/game_background.png').convert()
game_screen.fill((255, 255, 255))
pygame.display.update()
game_on, game_run = True, True
while game_on:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    game_screen.blit(game_background_image, (0, 0))
    pygame.display.flip()
    clock.tick(60)
