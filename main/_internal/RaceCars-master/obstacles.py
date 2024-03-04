import pygame
import random
from functions import load_image

FPS = 60


class WeakObstacle(pygame.sprite.Sprite):
    # Класс препятствий, которые при столкновении убавляют скорость
    def __init__(self, parent_rect, *group):
        super().__init__(*group)
        self.image = load_image(f'weak_obst_{random.randint(0, 1)}.png')
        # Тут в отличии от класса Car нужно передавать путь к картинке
        # Тут это не играет особой разницы, (в отличии от класса Car) так что можно поменять
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(61 + parent_rect.x, 190 + parent_rect.x)  # Генерируем случайное положение по x
        self.rect.y = random.randint(0 + parent_rect.y, 515 + parent_rect.y)  # Генерируем случайное положение по y

    def update(self, *args):
        self.rect = self.rect.move(0, args[0])


class StrongObstacle(pygame.sprite.Sprite):
    # Класс препятствий, которые при столкновении убавляют жизни
    def __init__(self, parent_rect, *group):
        super().__init__(*group)
        self.image = load_image(f'strong_obst_{random.randint(0, 1)}.png')  # Лучше пока не вызывать без картинок
        # Тут в отличии от класса Car нужно передавать путь к картинке
        # Тут это не играет особой разницы, (в отличии от класса Car) так что можно поменять
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(61 + parent_rect.x, 190 + parent_rect.x)  # Генерируем случайное положение по x
        self.rect.y = random.randint(0 + parent_rect.y, 515 + parent_rect.y)  # Генерируем случайное положение по y

    def update(self, *args):
        self.rect = self.rect.move(0, args[0])


class Bonus(pygame.sprite.Sprite):
    frame_count = 0

    def __init__(self, parent_rect, *groups):
        super().__init__()
        self.frames = []
        self.cut_sheet(load_image('bonus_animation.png'), 5, 4)
        self.cur_frame = 0
        self.add_speed = 1  # Прибавляемая скорость
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(61 + parent_rect.x, 190 + parent_rect.x)  # Генерируем случайное положение по x
        self.rect.y = random.randint(0 + parent_rect.y, 515 + parent_rect.y)  # Генерируем случайное положение по y
        while pygame.sprite.spritecollideany(self, groups[0]) is not None:
            self.rect.x = random.randint(61 + parent_rect.x, 190 + parent_rect.x)  # Генерируем случайное положение по x
            self.rect.y = random.randint(0 + parent_rect.y, 515 + parent_rect.y)  # Генерируем случайное положение по y
        for group in groups:
            group.add(self)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, *args):
        Bonus.frame_count %= 4
        if Bonus.frame_count == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(0, args[0])
        Bonus.frame_count += 1
