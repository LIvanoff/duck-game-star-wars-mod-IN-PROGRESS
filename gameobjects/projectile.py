from entitity import Entity
from tilemap import Tilemap
from config import BULLET_PROJECTILE_SPEED

class Projectile(Entity):
    def __init__(self, game, type : str, pos: tuple, size: tuple, lifetime) -> None:
        actualx = 0
        if not game.player.flip:
            actualx = pos[0] + game.player.size[0]
        else:
            actualx = pos[0]
        actualy = pos[1] + int(game.player.size[1] / 2)
        super().__init__(game, type, (actualx, actualy), size)
        # super().__init__(game, type, pos, size)
        self.flip = game.player.flip
        self.affectedByGravity = False
        self.frame = 0
        self.lifetime = lifetime
        self.dead = False