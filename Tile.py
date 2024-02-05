class Tile:
    def __init__(self, clazz : str, type : int, pos : tuple) -> None:
        self.clazz = clazz
        self.type  = type
        self.pos   = pos

    def toDict(self):
        return {
            'clazz' : self.clazz,
            'type'  : self.type,
            'pos'   : self.pos
        }

    @staticmethod
    def fromDict(dictTile : dict):
        return Tile(clazz=dictTile['clazz'], type=dictTile['type'], pos=tuple(dictTile['pos']))