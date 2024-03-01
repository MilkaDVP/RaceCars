import pygame
from start_screen import start_screen, gameover_screen
from game_cycle import game_cycle

# release 1.0

if __name__ == '__main__':
    # Инициализация pygame
    pygame.init()
    size = width, height = 620, 580
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Гонки 2D')

    car_image = start_screen(screen)
    running = True

    while running:
        game_cycle(screen, car_image)
        running = gameover_screen(screen)
    pygame.quit()
