import pygame
import Menu

pygame.init()
screen_size = (1000, 900)
start_menu = Menu.StartMenu(screen_size)
start_menu.start()
