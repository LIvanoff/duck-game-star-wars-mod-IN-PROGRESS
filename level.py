import pygame
from config import DEFAULT_TILESIZE
from tilemap import Tilemap
from tile import DEFAULT_TILESIZE, Tile

import json

class Level(Tilemap):
    def __init__(self, game, name, background, tileSize: int = DEFAULT_TILESIZE) -> None:
        super().__init__(game, tileSize)
        self.name = name
        self.background = background

    def save(self, path):
        onGridJsonable = {}
        for k, v in self.onGridTilemap.items():
            onGridJsonable[k] = v.toDict()

        offGridJsonable = list(map(lambda it: it.toDict(), self.offGridTilemap))

        with open(path, 'w') as savefile:
            json.dump(
                {
                    'name'           : self.name,
                    'background'     : self.background,
                    'onGridTilemap'  : onGridJsonable,
                    'tileSize'       : self.tileSize,
                    'offGridTilemap' : offGridJsonable
                },
                savefile
            )
 

    def load(self, path):
        with open(path, 'r') as loadfile:
            levelData = json.load(loadfile)
        
        for k, v in levelData['onGridTilemap'].items():
            self.onGridTilemap[k] = Tile.fromDict(v)
        self.tileSize = levelData['tileSize']
        self.offGridTilemap = list(map(lambda it: Tile.fromDict(it), levelData['offGridTilemap']))


    def render(self, surface: pygame.Surface, offset=[0,0], scale=0.5):
        surface.blit(pygame.transform.scale_by(self.game.bg_assets['bg_menu'], scale), (0, 0))
        super().render(surface, offset)