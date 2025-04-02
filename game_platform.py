from config import *
from load_image import load_image
from random import choice


class Platform(pygame.sprite.Sprite):
    """Класс платформ"""

    # Инициализация изображения
    platform_img = pygame.transform.scale(load_image('game/platform.png'), (59, 17))

    def __init__(self, group, x, y):
        super().__init__(group)
        """Инициализация"""
        self.x = x
        self.y = y

        self.image = Platform.platform_img
        self.rect = pygame.Rect(x, y, 59, 17)

    def updating(self, screen):
        """Отрисовка"""
        # Если платформа вышла за рамки окна
        if self.rect.y >= HEIGHT - 20:
            # Создаем новую
            self.rect.y = -20
            self.rect.x = choice(range(0, WIDTH - 60))

        screen.blit(self.image, self.rect)

    def top_rect(self):
        """Границы платформы"""
        left = self.rect.left + 3
        top = self.rect.top
        width = self.rect.width - 3
        height = self.rect.height

        return pygame.Rect(left, top, width, height)
