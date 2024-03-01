import os
import sys
import pygame


def terminate(record=None):
    """Функция сворачивает всю игру"""
    if record is not None:
        write_record('data/record.txt', record)
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    """Функция возвращает полный путь указанной картинки"""
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def read_record(filename, coding='utf8'):
    """Функция возвращает значение рекорда из файла"""
    with open(filename, encoding=coding, mode='r') as file:
        record = file.read().strip()
    return int(record)


def write_record(filename, record, coding='utf-8'):
    """Функция сохраняет значение рекорда в файл"""
    with open(filename, encoding=coding, mode='w') as file:
        if record is None:
            file.write('0')
        else:
            file.write(str(int(record)))
