import pygame
import sys

from config import *
from entities import Entity

from utils import loadImg, loadImgs

from tilemap import Tilemap


class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption(GAME_TITLE)

        self.assets = {
            'player'   : loadImg('images/characters/boba-fett/bobafett.png'),
            'crates'   : loadImgs('images/crates'),
            'platforms': loadImgs('images/platforms')
        }

        print(self.assets)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display = pygame.Surface((WIDTH / 2, HEIGHT / 2))
        self.clock = pygame.time.Clock()

        self.tilemap = Tilemap(self)

        self.player = Entity(self, 'player', (WIDTH / 4, HEIGHT / 4), (8, 15))
        

    def run(self):
        while True:
            self.display.fill((100, 100, 100))

            self.tilemap.render(self.display)

            self.player.update(((self.player.pMov[1] - self.player.pMov[0]) * 5, 0))
            self.player.render(self.display)

            self.handleEvents()

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

            pygame.display.update()
            self.clock.tick(CLOCK_TICKSPEED)

    
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.isMovingLeft()
                if event.key == pygame.K_d:
                    self.player.isMovingRight()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.player.notMovingLeft()
                if event.key == pygame.K_d:
                    self.player.notMovingRight()