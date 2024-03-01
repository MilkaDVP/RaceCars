import pygame
from functions import load_image, terminate
from car import Car
from button import Button

FPS = 50

pygame.init()
clock = pygame.time.Clock()


def start_screen(screen):
    # Размеры переданного экрана
    size = width, height = screen.get_rect().w, screen.get_rect().h
    intro_text = ["2D Гонки", "",
                  "Выберите машину"]

    # Добавляем картинку фона (я заменил на бесплатную картинку)
    fon = pygame.transform.scale(load_image('fon1.jpg'), (width, height))
    # Добавляем её на экран
    screen.blit(fon, (0, 0))
    # Создаём экземпляр шрифта
    font = pygame.font.Font(None, 30)
    text_coord = 50  # Начальная высота надписи
    # Рендерим текст стартового экрана построчно (из-за особенностей pygame)
    # тут я сам не до конца понимаю, поэтому лучше не трогать
    for line in intro_text:
        string_rendered = font.render(line, 1, (0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = width // 2 - intro_rect.w // 2
        text_coord += intro_rect.height
        fon.blit(string_rendered, intro_rect)

    # Создаём спрайты машин и кнопки
    car_sprites = pygame.sprite.Group()
    buttons = pygame.sprite.Group()
    btn = Button((200, 400), 'start_button.png', buttons)

    for i in range(4):
        Car((80 + i * 130, 200), load_image(f'car{i}.png'), car_sprites)

    selected_car = None
    selection_rect = pygame.Rect(-10, -10, 1, 1)  # Прямоугольник подсвечивающий выбранную машинку

    while True:
        screen.blit(fon, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for car in car_sprites:
                    # Проверяем на какую машину нажали мышкой и сохраняем выбор
                    if car.rect.collidepoint(event.pos):
                        selected_car = car
                        selection_rect = selected_car.rect
                # Если нажали кнопку и машина выбрана, то возвращаем выбранную машину и начинаем игру
                if btn.button_pressed(event.pos) and selected_car is not None:
                    return selected_car.image

        pygame.draw.rect(screen, (0, 0, 0), selection_rect)
        car_sprites.draw(screen)
        buttons.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def gameover_screen(screen):
    pygame.mixer.init()
    gayover = pygame.mixer.Sound('data/sounds/gameover1.wav')
    # Размеры переданного экрана
    size = width, height = screen.get_rect().w, screen.get_rect().h
    intro_text = ["Game over", "", "Игра окончена",
                  "Нажмите любую кнопку чтобы продолжить",
                  "Esc чтобы выйти"]
    image = load_image('gameover.jpg')
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
        gayover.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                return event.key != pygame.K_ESCAPE

        screen.blit(image, (0, 0))
        pygame.display.flip()
