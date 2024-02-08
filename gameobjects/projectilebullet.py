from gameobjects.projectile import Projectile
from tilemap import Tilemap
from config import *


class ProjectileBullet(Projectile):
    def __init__(self, game, type: str, pos: tuple, size: tuple, lifetime) -> None:
        super().__init__(game, type, pos, size, lifetime)
        self.affectedByGravity = False
        self.frame = 0
        self.lifetime = lifetime
        self.dead = False

    def update(self, tilemap: Tilemap):
        if self.flip: mov = (-BULLET_PROJECTILE_SPEED, 0)
        else: mov = (BULLET_PROJECTILE_SPEED, 0)
        super().update(tilemap, mov)

        if (self.collisions['right'] or self.collisions['left']):
            self.dead = True
                
        self.frame += 1
        if self.frame == self.lifetime:
            self.dead = True