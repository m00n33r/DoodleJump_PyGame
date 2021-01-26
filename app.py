from player import Player
from generator import *
from render import *
from camera import move_camera
from button import *
from config import *


def handle_events(events):
    global running, starting_screen, main_menu, play_game, \
        control_menu, player, platforms, game_over_screen, zero_height

    """Получение всех движений/нажатий в программе"""

    for event in events:

        if starting_screen:
            """Заставка"""

            # Отрисовка заставки
            draw_start_screen(screen)

            if event.type == pygame.QUIT:
                running = False

            # При нажатии любой клавиши
            elif event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                # Вход в главное меню
                starting_screen, main_menu = False, True

        if main_menu:
            """Главное меню"""

            # Создание кнопок
            new_game_button = Button(75, 300, 300, 100, (75, 200, 90),
                                     "Новая игра", (0, 0, 0), pixel_font_large)
            controls_button = Button(75, 410, 300, 100, (90, 170, 210),
                                     "Управление", (0, 0, 0), pixel_font_large)
            exit_button = Button(175, 520, 100, 50, (255, 50, 50),
                                 "Выйти", (0, 0, 0), pixel_font)

            # Отрисовка главного меню программы
            draw_main_menu(screen)

            # Отрисовка кнопок
            new_game_button.draw(screen)
            controls_button.draw(screen)
            exit_button.draw(screen)

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # При нажатии на кнопку выхода
                    if exit_button.is_clicked():
                        # Выход из программы
                        running = False

                    # При нажатии на кнопку "Новая игра"
                    if new_game_button.is_clicked():
                        # Вход в игру
                        main_menu, play_game = False, True

                        # Создание спрайтов
                        player = Player(200, 500, player_speed)
                        platforms = pygame.sprite.Group()
                        zero_height = 0
                        generating_platforms(platforms, 70)

                    if controls_button.is_clicked():
                        main_menu, control_menu = False, True

        if control_menu:
            """Меню управления"""
            draw_control_menu(screen)

            back_button = Button(175, 580, 100, 50, (255, 50, 50),
                                 "Назад", (0, 0, 0), pixel_font)
            back_button.draw(screen)

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back_button.is_clicked():
                        control_menu, main_menu = False, True

        if play_game:
            """Получение игровых движений"""
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Движение вправо/влево
                if event.key == pygame.K_a:
                    player.go_left()

                if event.key == pygame.K_d:
                    player.go_right()

            # Остановка движения
            if event.type == pygame.KEYUP:
                player.stop_going()

        if game_over_screen:
            """Окончание игры"""

            # Создание кнопок
            new_game_button = Button(75, 300, 300, 100, (75, 200, 90),
                                     "Сыграть еще раз", (0, 0, 0), pixel_font_large)
            main_menu_button = Button(75, 410, 300, 100, (90, 170, 210),
                                      "Вернуться в меню", (0, 0, 0), pixel_font_large)
            exit_button = Button(175, 520, 100, 50, (255, 50, 50),
                                 "Выйти", (0, 0, 0), pixel_font)

            # Отрисовка окона окончания
            draw_game_over_screen(screen, player)

            # Отрисовка кнопок
            new_game_button.draw(screen)
            main_menu_button.draw(screen)
            exit_button.draw(screen)

            # Проверка на нажатия
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if exit_button.is_clicked():
                        running = False

                    if new_game_button.is_clicked():
                        game_over_screen, play_game = False, True
                        player = Player(200, 500, player_speed)
                        platforms = pygame.sprite.Group()
                        zero_height = 0
                        generating_platforms(platforms, 70)

                    if main_menu_button.is_clicked():
                        game_over_screen, main_menu = False, True


if __name__ == '__main__':
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Doodle Jump')

    clock = pygame.time.Clock()

    while running:
        """Главный цикл"""

        # Получение всех движений/нажатий в программе
        handle_events(pygame.event.get())

        if play_game:
            """Игровой цикл"""
            # Отрисовка игры
            draw_game_screen(player, platforms, screen)
            # Обновление высоты
            zero_height = draw_score(screen, player, zero_height)
            # Если игрок вылетел за карту
            if not player.check_alive():
                # Убиваем его
                play_game, game_over_screen = False, True
            # Движение камеры
            move_camera(player, platforms)

        # Обновление экрана
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
