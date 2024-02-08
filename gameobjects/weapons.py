from entitity import Entity
from tilemap import Tilemap

from config import *


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
        self.pickUpCooldown = 0
        self.isPickedUp = False

    def shoot(self):
        self.game.sounds[f'{self.type}/shoot'].play()

    def statsFromDict(self, statsDict: dict):
        self.damage = statsDict['damage']
        self.ammo_num = statsDict['ammo_num']
        self.decay = statsDict['decay']

    def drop(self):
        self.isPickedUp = False
        self.pickUpCooldown = PICKUP_COOLDOWN
        if self.flip:
            self.pos = [self.pos[0] - self.game.player.size[0] * 2, self.pos[1]]
            self.vel[0] = -ITEM_DROP_VELOCITY
        else:
            self.pos = [self.pos[0] + self.game.player.size[0], self.pos[1]]
            self.vel[0] = ITEM_DROP_VELOCITY
        self.game.player.currentWeapon = None

    def update(self, tilemap: Tilemap, mov=(0, 0)):
        super().update(tilemap, mov)
        if self.pickUpCooldown > 0:
            self.pickUpCooldown -= 1
        else:
            if self.game.player.collisionRect().colliderect(self.collisionRect()):
                self.isPickedUp = True
                self.game.sounds['weapon/cocking'].play()
                self.game.player.currentWeapon = self

        if self.vel[0] > 0:
            self.vel[0] = max(self.vel[0] - 0.1, 0)
        else:
            self.vel[0] = min(self.vel[0] + 0.1, 0)
