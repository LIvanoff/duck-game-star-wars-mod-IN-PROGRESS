from entitity import Entity
from tilemap import Tilemap
from config import *

class Player(Entity):
    def __init__(self, game, pos: tuple, size: tuple) -> None:
        super().__init__(game, 'player', pos, size)
        self.airTime = 0
        self.animationOffset = (-3, -5)
        self.jumps = MAX_JUMPS
        self.wallslide = False
    

    def jump(self):
        if self.wallslide:
            print(self.lastMov)
            if self.flip and self.lastMov[0] < 0:
                self.vel[0] = JUMP_STRENGTH
                self.vel[1] = -JUMP_STRENGTH / 1.1
                self.airTime = 5
            if not self.flip and self.lastMov[0] > 0:
                self.vel[0] = -JUMP_STRENGTH
                self.vel[1] = -JUMP_STRENGTH / 1.1
                self.airTime = 5
        elif self.jumps:
            self.vel[1] = -4
            self.jumps -= 1
            self.airTime = 5

    
    def update(self, tilemap: Tilemap, mov=(0, 0)):
        super().update(tilemap, mov)

        self.airTime += 1
        if self.collisions['down']:
            self.airTime = 0
            self.jumps = MAX_JUMPS

        self.wallslide = False
        if (self.collisions['right'] or self.collisions['left']) and self.airTime > 4:
            self.wallslide = True
            self.vel[1] = min(self.vel[1], 0.5)
            if self.collisions['right']:
                self.flip = False
            else: self.flip = True
            self.setAction('wallslide')

        if not self.wallslide:
            if self.airTime > 4:
                self.setAction('jump')
            elif mov[0] != 0:
                self.setAction('run')
            else:
                self.setAction('idle')

        if self.vel[0] > 0:
            self.vel[0] = max(self.vel[0] - 0.1, 0)
        else:
            self.vel[0] = min(self.vel[0] + 0.1, 0)