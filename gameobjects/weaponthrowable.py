import pygame

from gameobjects.weapons import Weapon


class WeaponThrowable(Weapon):
    def __init__(self, game, type: str, pos: tuple, size: tuple, statsDict: dict) -> None:
        super().__init__(game, type, pos, size, statsDict)
        self.exlosion_time = statsDict['explosion_time']
        self.radius = statsDict['radius']
        self.shot_sound = statsDict['shot_sound_path']
        self.exlosion_sound = statsDict['explosion_sound_path']


class Grenade(WeaponThrowable):
    def __init__(self, game,
                 type: str,
                 pos: tuple,
                 size: tuple,
                 statsDict: dict
                 ):
        super().__init__(game, type, pos, size, statsDict)

    def exlosion(self):
        pygame.mixer.music.load(self.exlosion_sound)
        pygame.mixer.music.play()

    def throw(self):
        pass
