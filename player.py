from config import *
from images import *


class Player:
    """Класс игрока"""
    # Инициализация изображения персонажа
    player_img = pygame.transform.scale(load_image('game/player.png'), (50, 50))

    def __init__(self, x, y, speed):
        """Инициализация"""
        self.x = x
        self.y = y
        self.move_x = 0
        self.move_y = 0
        self.score = 0
        self.speed = speed
        self.right, self.left = True, False

        self.image = Player.player_img
        self.rect = self.image.get_rect()
        self.alive = True

    def update(self, platform_group, screen):
        """Обновления персонажа"""
        # Применить для игрока гравитацию
        self.gravitation()
        # При столкновении с платформой - прыгаем
        self.jumping(platform_group)

        # Сдвигаем песонажа в нужном направлении
        self.x = (self.x + self.move_x) % WIDTH
        self.y += self.move_y
        self.rect.x, self.rect.y = self.x, self.y

        # Отрисовка персонажа
        screen.blit(background, (0, 0))
        screen.blit(self.image, self.rect)

    def gravitation(self):
        """ Симуляция гравитации """
        # Каждый кадр увеличиваем его скогость падения
        self.move_y += 0.4

    def legs_rect(self):
        """Находим """
        x = self.rect.left + self.rect.width * 0.1
        y = self.rect.top + self.rect.height * 0.9
        width = self.rect.width * 0.6
        height = self.rect.height * 0.4

        return pygame.Rect(x, y, width, height)

    def jumping(self, platforms_group):
        """"""
        if self.move_y > 0:
            collided_platforms = pygame.sprite.spritecollide(self, platforms_group, False)
            for platform in collided_platforms:
                if self.legs_rect().colliderect(platform.top_rect()):
                    self.move_y = -10

    def go_left(self):
        """"""
        self.move_x = -self.speed
        if not self.left:
            self.image = pygame.transform.flip(self.image, True, False)
            self.right, self.left = False, True

    def go_right(self):
        """"""
        self.move_x = self.speed
        if not self.right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.right, self.left = True, False

    def stop_going(self):
        """"""
        self.move_x = 0

    def die(self):
        """"""
        if self.y > HEIGHT - self.rect.height:
            with open('data/saves/save_data.txt', 'r+') as best_score:
                max_score = float(best_score.readline().rstrip())
            if self.score > max_score:
                with open('data/saves/save_data.txt', 'w+') as best_score:
                    best_score.write('%.2f' % self.score)
            self.alive = False

    def check_alive(self):
        """"""
        self.die()
        return self.alive
