import pygame
import os


class Game(object):
    WIDTH = 600
    HEIGHT = 480

    def __init__(self, map_name):
        self.image = load_map(map_name)
        self.rect = self.image.get_rect()
        self.rect.center = (self.WIDTH / 2, self.HEIGHT / 2)

    def load_map(self, map_name: str):
        game_folder = os.path.dirname(__file__)
        assets_folder = os.path.join(game_folder, 'assets')
        img_folder = os.path.join(assets_folder, 'images')
        setting_folder = os.path.join(img_folder, 'map-setting')
        map_folder = os.path.join(setting_folder, 'hangar')
        player_img = pygame.image.load(os.path.join(map_folder, 'hangar-bnf.png')).convert()
        return player_img