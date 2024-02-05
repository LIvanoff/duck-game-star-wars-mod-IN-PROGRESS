class Tile:
    def __init__(self, clazz : str, type : int, pos : tuple) -> None:
        self.clazz = clazz
        self.type  = type
        self.pos   = pos