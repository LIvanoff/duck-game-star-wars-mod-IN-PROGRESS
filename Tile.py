import pygame

from config import *

class Tile:
    def __init__(self, clazz : str, type : int, pos : tuple) -> None:
        self.clazz = clazz
        self.type  = type
        self.pos   = pos
        if self.clazz in Tile.collideables():
            self.collideRect = pygame.Rect(self.pos[0] * DEFAULT_TILESIZE, self.pos[1] * DEFAULT_TILESIZE, DEFAULT_TILESIZE, DEFAULT_TILESIZE)
        else:
            self.collideRect = None

    def toDict(self):
        return {
            'clazz' : self.clazz,
            'type'  : self.type,
            'pos'   : self.pos
        }

    @staticmethod
    def fromDict(dictTile : dict):
        return Tile(clazz=dictTile['clazz'], type=dictTile['type'], pos=tuple(dictTile['pos']))
    
    @staticmethod
    def collideables():
        return ('crates', 'grass')
    
    @staticmethod
    def platofrms():
        return ('platforms', 'platforms_alt')
    
    @staticmethod
    def blocks():
        return ('grass', 'crates')