import pygame

from tile import *
from config import DEFAULT_TILESIZE


NEIGHBOR_OFFSETS = [(-1, 0), (-1, 1), (-1, -1), (0, 0), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]

class Tilemap:
    def __init__(self, game, tileSize : int = DEFAULT_TILESIZE) -> None:
        self.game = game
        self.tileSize = tileSize
        self.onGridTilemap = {}
        self.offGridTilemap = []

        self.mockTiles()


    def tilesAround(self, pos : tuple):
        gridPos = (int(pos[0] // self.tileSize), int(pos[1] // self.tileSize))

    
    def mockTiles(self):
        for idx in range(45):
            self.onGridTilemap[f'{idx}:20'] = Tile(clazz="crates", type=1, pos=(idx, 20))
            # self.onGridTilemap[f'4:{1 + idx}'] = Tile(clazz="crates", type=2, pos=(4, 1+idx))


    def render(self, surface : pygame.Surface):
        for tile in self.offGridTilemap:
            surface.blit(self.game.assets[tile.clazz][tile.type], (tile.pos[0], tile.pos[1]))

        for _, tile in self.onGridTilemap.items():
            surface.blit(self.game.assets[tile.clazz][tile.type], (tile.pos[0] * self.tileSize, tile.pos[1] * self.tileSize))
