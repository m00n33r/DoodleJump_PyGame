from platform import Platform
from random import choice
from config import *


def generate_platform(group, y):
    """Рандмное положение по оси Х"""
    x = choice(range(0, WIDTH - 60))
    Platform(group, x, y)


def generating_platforms(group, going):
    """Генерация платформ"""
    y = 5
    while y < HEIGHT:
        generate_platform(group, y)
        y += going
    Platform(group, 200, 600)
