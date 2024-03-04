import pygame
from functions import load_image, terminate

pygame.init()


def pause(screen, record):
    size = width, height = screen.get_rect().w, screen.get_rect().h
    image = load_image('pause_fon.jpg')
    intro_text = ["Пауза", "Нажмите Esc, чтобы продолжить"]

    # Создаём экземпляр шрифта
    font = pygame.font.Font(None, 30)
    text_coord = 260  # Начальная высота надписи
    # Рендерим текст стартового экрана построчно (из-за особенностей pygame)
    # тут я сам не до конца понимаю, поэтому лучше не трогать
    for line in intro_text:
        string_rendered = font.render(line, 1, (255, 255, 255))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = width // 2 - intro_rect.w // 2
        text_coord += intro_rect.height
        image.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate(record=record)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        screen.blit(image, (0, 0))
        pygame.display.flip()
