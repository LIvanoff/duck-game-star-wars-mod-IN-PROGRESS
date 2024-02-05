import pygame


class Entity:
    def __init__(self, game, type : str, pos : tuple, size) -> None:
        self.game = game
        self.type = type
        self.pos  = list(pos)
        self.size = size
        self.velocity = [0, 0]

    def update(self, mov=(0, 0)):
        frame_movement