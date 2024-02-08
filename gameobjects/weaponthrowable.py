import pygame

from gameobjects.weapons import Weapon
from config import WIDTH, HEIGHT


class WeaponThrowable(Weapon):
    def __init__(self, game, type: str, pos: tuple, size: tuple, statsDict: dict) -> None:
        super().__init__(game, type, pos, size, statsDict)
        self.gravity = 9.8
        self.exlosion_time = statsDict['explosion_time']
        self.radius = statsDict['radius']
        self.shot_sound = statsDict['shot_sound_path']
        self.exlosion_sound = statsDict['explosion_sound_path']

# class Grenade(WeaponThrowable):
#     def __init__(self, game,
#                  type: str,
#                  pos: tuple,
#                  size: tuple,
#                  statsDict: dict
#                  ):
#         super().__init__(game, type, pos, size, statsDict)
#         self.vel_y = -11
#         self.speed = 7

#     def exlosion(self):
#         pygame.mixer.music.load(self.exlosion_sound)
#         pygame.mixer.music.play()
#         return True

#     def throw(self, direction):
#         self.vel_y += self.gravity
#         dx = direction * self.speed
#         dy = self.vel_y

#         # update grenade position
#         self.pos[0] += dx
#         self.pos[1] += dy

#         self.exlosion_time -= 1
#         if self.exlosion_time <= 0:
#             self.isBlowup = self.exlosion()
