from gameobjects.weapons import Weapon
from gameobjects.projectilebullet import ProjectileBullet
from config import CLOCK_TICKSPEED

class WeaponWithProjectile(Weapon):
    def __init__(self, game, type: str, pos: tuple, size: tuple, statsDict: dict) -> None:
        super().__init__(game, type, pos, size, statsDict)
        self.lastShotFrame = 0
        
    def shoot(self):
        if self.frame - self.lastShotFrame >= self.decay:
            super().shoot()
            self.game.projectiles.append(ProjectileBullet(self.game, 'projectile_red', self.pos, (8, 3), lifetime=60))
            self.lastShotFrame = self.frame