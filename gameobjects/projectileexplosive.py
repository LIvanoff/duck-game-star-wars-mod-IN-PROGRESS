from gameobjects.projectile import Projectile
from tilemap import Tilemap
from config import *


class ProjectileExplosive(Projectile):
    def __init__(self, game, type: str, pos: tuple, size: tuple, lifetime) -> None:
        super().__init__(game, type, pos, size, lifetime)
        self.affectedByGravity = True

    def explode(self):
        self.game.sounds[f'{self.type}/explode'].play()

    def update(self, tilemap: Tilemap):
        # Переделать, а то она скачет лол
        if self.flip: mov = (-EXPLOSIVE_PROJECTILE_SPEED, -3)
        else: mov = (EXPLOSIVE_PROJECTILE_SPEED, -3)
        super().update(tilemap, mov)

        if self.vel[0] > 0:
            self.vel[0] = max(self.vel[0] - 1, 0)
        else:
            self.vel[0] = min(self.vel[0] + 1, 0)

        self.frame += 1
        if self.frame == self.lifetime:
            self.explode()
            self.dead = True
            