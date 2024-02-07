from entitity import Entity
from tilemap import Tilemap

class Weapon(Entity):
    def __init__(self, 
                 game, 
                 type : str,
                 pos: tuple, 
                 size: tuple,
                 damage: int = 10,
                 decay: int = 10, 
                 ammo_num: int = 100
    ) -> None:
        super().__init__(game, type, pos, size)
        self.damage = damage
        self.ammo_num = ammo_num
        self.decay = decay

        self.isPickedUp = False


    def statsFromDict(self, statsDict : dict):
        self.damage = statsDict['damage']
        self.ammo_num = statsDict['ammo_num']
        self.decay = statsDict['decay']


    def update(self, tilemap: Tilemap, mov=(0, 0)):
        super().update(tilemap, mov)
        if self.game.player.collisionRect().colliderect(self.collisionRect()):
            self.isPickedUp = True
            self.game.player.currentWeapon = self