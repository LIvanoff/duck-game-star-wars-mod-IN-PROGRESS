import pygame

from Tile import Tile
from config import DEFAULT_TILESIZE

class Tilemap:
    def __init__(self, tileSize : int = DEFAULT_TILESIZE) -> None:
        self.tileSize = tileSize
        self.onGridTilemap = {}
        self.offGridTilemap = []

    
    def mockTiles(self):
        for idx in range(10):
            self.onGridTilemap[f'{3 + idx}:10'] = Tile(clazz="platforms", type="hangar_platform0", pos=(3+idx, 10))
            self.onGridTilemap[f'10:{5 + idx}'] = Tile(clazz="crates", type="crate_red", pos=(10, 5+idx))


    