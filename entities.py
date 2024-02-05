import pygame


class Entity:
    facing = False

    def __init__(self, game, type : str, pos : tuple, size) -> None:
        self.game = game
        self.type = type
        self.pos  = list(pos)
        self.size = size
        self.vel = [0, 0]
        self.pMov = [False, False]

    
    def update(self, mov=(0, 0)):
        frameMov = (mov[0] + self.vel[0], mov[1] + self.vel[1])

        self.pos[0] += frameMov[0]
        self.pos[1] += frameMov[1]

        # self.vel[1] = min(5, self.vel[1] + 0.1)

    
    def isMovingRight(self):
        self.facing = False
        self.pMov[1] = True

    def notMovingRight(self):
        self.pMov[1] = False

    def isMovingLeft(self):
        self.facing = True
        self.pMov[0] = True

    def notMovingLeft(self):
        self.pMov[0] = False

    
    def render(self, surface : pygame.Surface):
        surface.blit(pygame.transform.flip(self.game.assets['player'], self.facing, False), self.pos)