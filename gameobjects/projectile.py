from entitity import Entity
from tilemap import Tilemap
from config import PROJECTILE_SPEED

class Projectile(Entity):
    def __init__(self, game, type : str, pos: tuple, size: tuple, lifetime) -> None:
        actualx = 0
        if not game.player.flip:
            actualx = pos[0] + game.player.size[0]
        else:
            actualx = pos[0]
        actualy = pos[1] + int(game.player.size[1] / 2)
        super().__init__(game, type, (actualx, actualy), size)
        self.flip = game.player.flip
        self.frame = 0
        self.lifetime = lifetime
        self.dead = False
    
    def update(self, tilemap: Tilemap):
        if self.flip: mov = (-PROJECTILE_SPEED, 0)
        else: mov = (PROJECTILE_SPEED, 0)
        
        super().update(tilemap, mov)

        if (self.collisions['right'] or self.collisions['left']):
            self.dead = True
                
        self.frame += 1
        if self.frame == self.lifetime:
            self.dead = True