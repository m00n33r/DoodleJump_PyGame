from src.utils.images import *
from src.utils.fonts import *


def draw_start_screen(screen):
    screen.blit(background, (0, 0))
    screen.blit(big_logo, (0, 140))
    screen.blit(pixel_font_large.render("Doodle Jump", True,
                                        pygame.Color('black')), (30, 120, 50, 20))
    screen.blit(pixel_font.render("press any key to start..",
                                  True, pygame.Color('black')), (150, 643, 50, 20))


def draw_main_menu(screen):
    screen.blit(background, (0, 0))

    screen.blit(tiny_logo, (300, -20))

    screen.blit(pixel_font_large.render("Doodle Jump", True,
                                        pygame.Color('black')), (30, 120, 50, 20))


def draw_control_menu(screen):
    screen.blit(background, (0, 0))
    screen.blit(tiny_logo, (300, -20))
    screen.blit(controls_image, (50, 275))
    screen.blit(pixel_font_large.render("Doodle Jump", True,
                                        pygame.Color('black')), (30, 120, 50, 20))
    screen.blit(pixel_font.render("Управление:", True,
                                  pygame.Color('black')), (60, 220, 50, 20))
    screen.blit(pixel_font.render("  A - Полёт налево",
                                  True, pygame.Color('black')), (70, 250, 50, 20))
    screen.blit(pixel_font.render("  D - Полет направо",
                                  True, pygame.Color('black')), (70, 280, 50, 20))


def draw_game_screen(player, platforms, screen):
    player.update(platforms, screen)

    for platform in platforms:
        platform.updating(screen)


def draw_game_over_screen(screen, player):
    with open('data/saves/save_data.txt') as best_score:
        max_score = float(best_score.readline().rstrip())

    game_over_text = pixel_font_large.render("Game Over", True,
                                             pygame.Color('whitesmoke'))
    score_text = pixel_font.render(f"Your score: {'%.2f' % player.score}", True,
                                   pygame.Color('whitesmoke'))
    max_score_text = pixel_font.render(f"Best score: {'%.2f' % max_score}", True,
                                   pygame.Color('whitesmoke'))

    screen.blit(background, (0, 0))
    screen.blit(overlay_img, (0, 0))
    screen.blit(game_over_text, (75, 100))
    screen.blit(max_score_text, (73, 220))
    screen.blit(score_text, (73, 255))
    if max_score <= float('%.2f' % player.score):
        best_score_text = pixel_font.render("New best score!!", True, pygame.Color('whitesmoke'))
        screen.blit(best_score_text, (60, 180))


def draw_score(screen, player, zero_height):
    pygame.draw.rect(screen, (0, 157, 254), (0, 0, 450, 50))
    pygame.draw.line(screen, pygame.Color('black'), (0, 50), (450, 50), 7)

    zero_height -= player.move_y
    player.score = max(player.score, zero_height / 5)
    score = pixel_font.render('%.2f' % player.score, True,
                              pygame.Color('black'))
    screen.blit(score, (20, 10))

    return zero_height
