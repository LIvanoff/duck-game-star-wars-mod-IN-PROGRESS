import pygame

from tilemap import *

# TODO: Создать класс BaseEntity без ускорений и лишних элементов
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
        self.animationOffset = (0, 0)
        self.lastMov = [0, 0]
        self.currentAction = ''
        self.affectedByGravity = True
        self.setAction('idle')


    def collisionRect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    

    def setAction(self, action : str):
        if action != self.currentAction:
            self.currentAction = action
            self.animation = self.game.animations[f'{self.type}/{action}'].copy()

    
    def update(self, tilemap : Tilemap, mov=(0, 0)):
        '''
        Функция апдейта работающая с тайлами а не боксами коллизий
        '''

        self.collisions = {'up' : False, 'down' : False, 'left' : False, 'right' : False}
        
        frameMov = (mov[0] + self.vel[0], mov[1] + self.vel[1])

        self.pos[0] += frameMov[0]
        entityRect = self.collisionRect()
        for tile in tilemap.collisionTiles(self):
            if entityRect.colliderect(tile.collisionRect):
                if frameMov[0] > 0:
                    if tile.clazz not in Tile.platforms():
                        entityRect.right = tile.collisionRect.left
                        self.collisions['right'] = True
                if frameMov[0] < 0:
                    if tile.clazz not in Tile.platforms():
                        entityRect.left = tile.collisionRect.right
                        self.collisions['left'] = True
                self.pos[0] = entityRect.x

        self.pos[1] += frameMov[1]
        entityRect = self.collisionRect()
        for tile in tilemap.collisionTiles(self):
            if entityRect.colliderect(tile.collisionRect):
                if frameMov[1] > 0:
                    if tile.clazz not in Tile.platforms():
                        entityRect.bottom = tile.collisionRect.top
                        self.collisions['down'] = True
                    else:
                        if tile.collisionRect.collidepoint(entityRect.midbottom):
                            entityRect.bottom = tile.collisionRect.top
                            self.collisions['down'] = True
                if frameMov[1] < 0:
                    if tile.clazz not in Tile.platforms():
                        entityRect.top = tile.collisionRect.bottom
                        self.collisions['up'] = True
                self.pos[1] = entityRect.y

        self.lastMov = mov

        if self.affectedByGravity:
            self.vel[1] = min(5, self.vel[1] + 0.1)

        if self.collisions['down'] or self.collisions['up']:
            self.vel[1] = 0

        self.animation.update()

    
    def render(self, surface : pygame.Surface, offset = [0, 0]):
        surface.blit(
            pygame.transform.flip(self.animation.img(), self.flip, False), 
            (self.pos[0] - offset[0] + self.animationOffset[0], self.pos[1] - offset[1] + self.animationOffset[1])
        )