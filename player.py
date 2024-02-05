from entitity import Entity
from tilemap import Tilemap

class Player(Entity):
    def __init__(self, game, type: str, pos: tuple, size: tuple) -> None:
        super().__init__(game, 'player', pos, size)
        self.airTime = 0
    
    def update(self, tilemap: Tilemap, mov=(0, 0)):
        super().update(tilemap, mov)

        self.airTime += 1
        if self.collisions['down']:
            self.airTime = 0

        if self.airTime > 4:
            self.setAction('jump')
        elif mov[0] != 0:
            self.setAction('run')
        else:
            self.setAction('idle')