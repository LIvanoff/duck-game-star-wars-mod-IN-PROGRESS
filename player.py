from pygame import Surface
from entitity import Entity
from tilemap import Tilemap
from config import *
from gameobjects.weapons import Weapon

class Player(Entity):
    def __init__(self, game, pos: tuple, size: tuple) -> None:
        super().__init__(game, 'player', pos, size)
        self.airTime = 0
        self.animationOffset = (-3, -5)
        self.jumps = MAX_JUMPS
        self.wallslide = False
        self.currentWeapon : Weapon = None
        self.direction = 1
        self.health = 100


    def jump(self):
        if self.wallslide:
            if self.flip and self.lastMov[0] < 0:
                self.vel[0] = JUMP_STRENGTH
                self.vel[1] = -JUMP_STRENGTH / 1.1
                self.airTime = 5
            if not self.flip and self.lastMov[0] > 0:
                self.vel[0] = -JUMP_STRENGTH
                self.vel[1] = -JUMP_STRENGTH / 1.1
                self.airTime = 5
        elif self.jumps:
            self.vel[1] = -JUMP_STRENGTH
            self.jumps -= 1
            self.airTime = 5


    def isMovingRight(self):
        self.flip = False
        self.pMov[1] = True
        self.direction = 1

    def notMovingRight(self):
        self.pMov[1] = False

    def isMovingLeft(self):
        self.flip = True
        self.pMov[0] = True
        self.direction = -1

    def notMovingLeft(self):
        self.pMov[0] = False

    
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
            if self.currentWeapon:
                self.setAction(f'wallslide_{self.currentWeapon.type}')
            else:
                self.setAction('wallslide')


        if not self.wallslide:
            if self.airTime > 4:
                if self.currentWeapon:
                    self.setAction(f'jump_{self.currentWeapon.type}')
                else: self.setAction('jump')
            elif mov[0] != 0:
                if self.currentWeapon:
                    self.setAction(f'run_{self.currentWeapon.type}')
                else: self.setAction('run')
            else:
                if self.currentWeapon:
                    self.setAction(f'idle_{self.currentWeapon.type}')
                else: self.setAction('idle')

        if self.vel[0] > 0:
            self.vel[0] = max(self.vel[0] - 0.1, 0)
        else:
            self.vel[0] = min(self.vel[0] + 0.1, 0)


        if self.currentWeapon:
            self.currentWeapon.pos = self.pos
            self.currentWeapon.frame += 1
            self.currentWeapon.removeDeadProjectiles()
            self.currentWeapon.flip = self.flip
            for projectile in self.currentWeapon.projectiles:
                projectile.update(tilemap)
    
    def render(self, surface: Surface, offset=[0, 0]):
        super().render(surface, offset)

        if self.currentWeapon:
            for projectile in self.currentWeapon.projectiles:
                projectile.render(surface, offset)