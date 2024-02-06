import pygame

from tilemap import *

class Entity:
    flip = False

    def __init__(self, game, type : str, pos : tuple, size : tuple) -> None:
        self.game = game
        self.type = type
        self.pos  = list(pos)
        self.size = size
        self.vel = [0, 0]
        self.pMov = [False, False]
        self.collisions = {'up' : False, 'down' : False, 'left' : False, 'right' : False}
        self.currentAction = ''
        self.animationOffset = (-3, -3)
        self.setAction('idle')


    def collisionRect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    

    def setAction(self, action : str):
        if action != self.currentAction:
            self.currentAction = action
            self.animation = self.game.animations[f'{self.type}/{action}'].copy()
    

    def update(self, tilemap : Tilemap, mov=(0, 0)):
        self.collisions = {'up' : False, 'down' : False, 'left' : False, 'right' : False}
        
        frameMov = (mov[0] + self.vel[0], mov[1] + self.vel[1])

        self.pos[0] += frameMov[0]
        entityRect = self.collisionRect()
        for rect in tilemap.collisionRects(self):
            if entityRect.colliderect(rect):
                if frameMov[0] > 0:
                    entityRect.right = rect.left
                    self.collisions['right'] = True
                if frameMov[0] < 0:
                    entityRect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entityRect.x

        self.pos[1] += frameMov[1]
        entityRect = self.collisionRect()
        for rect in tilemap.collisionRects(self):
            if entityRect.colliderect(rect):
                if frameMov[1] > 0:
                    entityRect.bottom = rect.top
                    self.collisions['down'] = True
                if frameMov[1] < 0:
                    entityRect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entityRect.y

        self.vel[1] = min(5, self.vel[1] + 0.1)

        if self.collisions['down'] or self.collisions['up']:
            self.vel[1] = 0

        self.animation.update()

    
    def isMovingRight(self):
        self.flip = False
        self.pMov[1] = True

    def notMovingRight(self):
        self.pMov[1] = False

    def isMovingLeft(self):
        self.flip = True
        self.pMov[0] = True

    def notMovingLeft(self):
        self.pMov[0] = False

    
    def render(self, surface : pygame.Surface, offset = [0, 0]):
        # surface.blit(self.game.assets['player'], self.pos)
        surface.blit(
            pygame.transform.flip(self.animation.img(), self.flip, False), 
            (self.pos[0] - offset[0] + self.animationOffset[0], self.pos[1] - offset[1] + self.animationOffset[1])
        )