from gameobjects.weaponthrowable import WeaponThrowable
from gameobjects.projectileexplosive import ProjectileExplosive


class Grenade(WeaponThrowable):
    def __init__(self, game, type: str, pos: tuple, size: tuple, statsDict: dict) -> None:
        super().__init__(game, type, pos, size, statsDict)
        self.isThrown = False
        self.lastShotFrame = 0

    def shoot(self):
        if self.frame - self.lastShotFrame >= self.decay:
            super().shoot()
            self.isThrown = True
            self.game.player.currentWeapon = None
            self.game.projectiles.append(ProjectileExplosive(self.game, f'projectile_{self.type}', self.pos, self.size, lifetime=100))
            self.lastShotFrame = self.frame