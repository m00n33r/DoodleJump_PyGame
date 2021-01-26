from fonts import *


class Button:
    """Класс кнопки на экране"""
    def __init__(self, x, y, length_x, length_y, color, text, text_color, font):
        """Инициализация"""
        self.x = x
        self.y = y
        self.width = length_x
        self.height = length_y
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rendered_text = pixel_font.render(self.text, True, self.text_color)
        self.text_rect = self.rendered_text.get_rect()
        self.text_rect.center = self.rect.center

    def is_clicked(self):
        """Проверка на нажатие"""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.x < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.height:
            return True
        else:
            return False

    def draw(self, screen):
        """Отрисовка"""
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, self.text_color, self.rect, 5)
        screen.blit(self.rendered_text, (self.text_rect.x, self.text_rect.y))
