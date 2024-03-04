import pygame
import random
from functions import load_image
from obstacles import WeakObstacle, StrongObstacle, Bonus

pygame.init()
screen = pygame.display.set_mode((620, 580))


class RoadBlock(pygame.sprite.Sprite):
    image = load_image('road.png')
    speed = 3

    def __init__(self, x, y, *group):
        # Обращение к конструктору родительского класса и добавление спрайта в группы
        super().__init__(*group)
        self.image = RoadBlock.image
        self.speed = RoadBlock.speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.objects = pygame.sprite.Group()  # Группа спрайтов для объектов на блоке дороги

    def add_object(self, weak_obst, strong_obst, bonuses):
        """Функция добавляет объект на блок дороги"""
        eval("{0}Obstacle(self.rect, self.objects, {1})".format(
            *random.choice([('Weak', 'weak_obst'), ('Strong', 'strong_obst')])))
        ran = random.choice([0, 0, 0, 0, 0, 1])
        if ran:
            Bonus(self.rect, self.objects, bonuses)

    def update(self):
        """Функция обновляет позицию блока дороги"""
        self.rect = self.rect.move(0, RoadBlock.speed)
        self.objects.update(RoadBlock.speed)

    def change_speed(self, speedplus):
        """Функция меняет скорость движения"""
        if RoadBlock.speed < 11 or speedplus < 0:
            RoadBlock.speed += speedplus

    def is_viewing(self):
        """Функция проверяет не выходит ли блок за границы экрана"""
        return self.rect.y <= 580
