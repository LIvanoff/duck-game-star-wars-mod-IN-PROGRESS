import os
import pygame

from config import ASSETS_PATH

def load_map(map_name: str):
    game_folder = os.path.dirname(__file__)
    assets_folder = os.path.join(game_folder, 'assets')
    img_folder = os.path.join(assets_folder, 'images')
    setting_folder = os.path.join(img_folder, 'map-setting')
    map_folder = os.path.join(setting_folder, 'hangar')
    player_img = pygame.image.load(os.path.join(map_folder, 'hangar-bnf.png')).convert()
    return player_img


def loadImg(path : str):
    img = pygame.image.load(ASSETS_PATH + path)
    return img