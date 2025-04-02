from config import *
from load_image import load_image

"""Инициализация изображений"""

# Фоновые
background = load_image('backgrounds/background.jpg')
overlay_img = pygame.transform.scale(load_image
                                     ('backgrounds/black_overlay.png'), (WIDTH, HEIGHT))
overlay_img.set_alpha(150)

# Логотипы
big_logo = pygame.transform.scale(load_image('other_images/logo.jpg', -1), (450, 450))
tiny_logo = pygame.transform.scale(load_image('other_images/logo.jpg', -1), (150, 150))

# Остальное
controls_image = pygame.transform.scale(load_image
                                        ('other_images/controls_image.jpg', -1), (350, 330))
