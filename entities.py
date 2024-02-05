import pygame


class Entity:
    def __init__(self, game, type : str, pos : tuple, size) -> None:
        self.game = game
        self.type = type
        self.pos  = list(pos)
        self.size = size
        self.vel = [0, 0]

    
    def update(self, mov=(0, 0)):
        frameMov = (mov[0] + self.vel[0], mov[1] + self.vel[1])
        
        self.pos[0] += frameMov[0]
        self.pos[1] += frameMov[1]

    
    def render(self, surface):
        surface.blit(self.game.assets['player'], self.pos)