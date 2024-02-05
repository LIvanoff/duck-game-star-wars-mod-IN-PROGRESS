import pygame
import sys

from config import *


class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption(GAME_TITLE)

        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        
    def run(self):
        while True:
            # self.display.fill()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(CLOCK_TICKSPEED)