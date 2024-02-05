import pygame
import os
from utils import load_map
from config import *
import random


class Map(pygame.sprite.Sprite):
    WIDTH = 600
    HEIGHT = 480

    def __init__(self, map_name):
        pygame.sprite.Sprite.__init__(self)
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


class LocationQueue(object):
    def __init__(self):
        self.queue = []

    def push(self, location):
        self.queue.append(location)

    def generate_location(self):
        for i in range(ROUNDS):
            self.push(random.choice(LOCATION))

    def get_location(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:
            return IndexError

    def size(self):
        return len(self.queue)

# lq = LocationQueue()
# lq.generate_location()
# for i in range(ROUNDS):
#     print(lq.get_location())
