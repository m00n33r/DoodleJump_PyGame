def move_camera(player, platforms):
    """Движение камеры"""
    if player.y < 255:
        # Сдвиг спрайтов
        for platform in platforms:
            platform.rect.y -= player.move_y
        player.y -= player.move_y
