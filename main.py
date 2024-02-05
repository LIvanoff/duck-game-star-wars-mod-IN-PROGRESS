import pygame
from gameobjects.maps import Map
import random

WIDTH = 1280
HEIGHT = 720
FPS = 60


def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("duck game mode")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    map = Map('hangar')
    all_sprites.add(map)

    # Цикл игры
    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # проверка для закрытия окна
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        all_sprites.update()

        # Рендеринг
        all_sprites.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()

