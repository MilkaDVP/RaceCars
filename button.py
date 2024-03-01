import pygame
from functions import load_image


class Button(pygame.sprite.Sprite):
    def __init__(self, cords, sprite_path, *groups):
        super().__init__(*groups)
        self.image = load_image(sprite_path)
        self.rect = self.image.get_rect()
        self.rect.x = cords[0]
        self.rect.y = cords[1]

    def button_pressed(self, pos):
        return self.rect.collidepoint(pos)
