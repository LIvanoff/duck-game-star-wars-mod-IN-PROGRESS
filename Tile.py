class Tile:
    def __init__(self, clazz : str, type : str, pos : tuple) -> None:
        self.clazz = clazz
        self.type  = type
        self.pos   = pos