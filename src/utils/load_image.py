import pygame
import os
import sys


def load_image(name, colorkey=None):
    """Загрузка изображений"""

    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 1))
        image.set_colorkey(colorkey)
    else:
        pass

    return image
