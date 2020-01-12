import pygame
import sys
import Menu
import Snake


class Game:
    def __init__(self, screen_size):

        self.score = 0
        self.screen_size = screen_size
        self.x, self.y = self.screen_size
        self.menu_screen = pygame.display.set_mode(screen_size)
        self.menu_background_image = pygame.image.load('data/game_background.png').convert()
        self.clock = pygame.time.Clock()
        pygame.display.update()

    def start(self):
        count = 0
        snake = Snake.Snake(self.x, self.y)
        food = Snake.Food(self.x, self.y)
        self.pause_on = True
        while self.pause_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        snake.check_direction("RIGHT")
                    elif event.key == pygame.K_LEFT or event.key == ord('a'):
                        snake.check_direction("LEFT")
                    elif event.key == pygame.K_UP or event.key == ord('w'):
                        snake.check_direction("UP")
                    elif event.key == pygame.K_DOWN or event.key == ord('s'):
                        snake.check_direction("DOWN")
                    elif event.key == pygame.K_ESCAPE:
                        menu = Menu.PauseMenu(self.screen_size)
                        menu.start()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_click(event.pos)
            self.menu_screen.blit(self.menu_background_image, (0, 0))
            snake.change_head_pos()
            value = snake.check_snake(food.get_pos(), food.size[0])
            if value:
                self.score += 1
                food.update()
            snake.check_collision(self)
            snake.draw_snake(self.menu_screen)
            self.menu_screen.blit(food.image, food.rect)
            self.show_score()
            pygame.display.flip()
            self.clock.tick(20)
            count += 1
            self.show_score()

    def get_click(self, coords):
        x, y = coords
        if x <= 65 and y <= 65:
            menu = Menu.PauseMenu(self.screen_size)
            menu.start()
        print(coords)

    def show_score(self):
        score_font = pygame.font.SysFont('tahoma', 50)
        score_surf = score_font.render('Score: {0}'.format(self.score), True, pygame.Color(255, 255, 255))
        score_rect = score_surf.get_rect()
        score_rect.midtop = (193, 5)
        self.menu_screen.blit(score_surf, score_rect)

    def game_over(self):
        lose_menu = Menu.LoseMenu(self.screen_size)
        lose_menu.start()

    def terminate(self):
        pygame.quit()
        sys.exit()
