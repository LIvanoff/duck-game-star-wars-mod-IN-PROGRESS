from gameobjects.weapons import Weapon
from gameobjects.projectile import Projectile
from config import CLOCK_TICKSPEED

class WeaponWithProjectile(Weapon):
    def __init__(self, game, type: str, pos: tuple, size: tuple, statsDict: dict) -> None:
        super().__init__(game, type, pos, size, statsDict)
        self.projectiles = []
        self.decay = statsDict['decay'] * CLOCK_TICKSPEED
        self.frame = statsDict['decay'] * CLOCK_TICKSPEED
        self.lastShotFrame = 0
        
    def shoot(self):
        if self.frame - self.lastShotFrame >= self.decay:
            super().shoot()
            self.projectiles.append(Projectile(self.game, 'projectile_red', self.pos, (8, 3), lifetime=60))
            self.lastShotFrame = self.frame


    def removeDeadProjectiles(self):
        self.projectiles = [x for x in self.projectiles if not x.dead]