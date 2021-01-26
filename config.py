import pygame

pygame.init()

running = True
WIDTH, HEIGHT = (450, 700)
FPS = 60

# Создаем переменные для простого понимания где мы находимся
starting_screen = True
main_menu = False
escape_menu = False
control_menu = False
play_game = False
game_over_screen = False

# Настройки персонажа
player_speed = 8
