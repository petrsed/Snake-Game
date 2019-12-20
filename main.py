import pygame
import Menu

pygame.init()
screen_size = (1000, 900)
menu = Menu.MainMenu(screen_size)
menu.start()
