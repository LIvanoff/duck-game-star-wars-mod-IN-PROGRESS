import pygame
from pygame import mixer

from entitity import Entity
from tilemap import Tilemap


class Weapon(Entity):
    def __init__(self,
                 game,
                 type: str,
                 pos: tuple,
                 size: tuple,
                 statsDict: dict
                 ) -> None:
        super().__init__(game, type, pos, size)
        self.damage = statsDict['damage']
        self.ammo_num = statsDict['ammo_num']
        self.decay = statsDict['decay']
        self.shot_sound = statsDict['shot_sound_path']

        self.isPickedUp = False

    
    def shoot(self):
        shootSound = self.game.sounds[f'{self.type}/shoot']
        shootSound.play()


    def statsFromDict(self, statsDict: dict):
        self.damage = statsDict['damage']
        self.ammo_num = statsDict['ammo_num']
        self.decay = statsDict['decay']

    def update(self, tilemap: Tilemap, mov=(0, 0)):
        super().update(tilemap, mov)
        if self.game.player.collisionRect().colliderect(self.collisionRect()):
            self.isPickedUp = True
            self.game.player.currentWeapon = self

