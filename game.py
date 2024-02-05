import pygame
import sys

from config import *
from entitity import Entity
from player import Player

from utils import loadImg, loadImgs

from tilemap import Tilemap
from animation import Animation


class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption(GAME_TITLE)

        self.assets = {
            'player'   : loadImg('images/characters/boba-fett/bobafett.png'),
            'crates'   : loadImgs('images/crates'),
            'platforms': loadImgs('images/platforms'),
            'bg_menu'  : loadImg('images/map-setting/hangar/hangar-bg.png'),
            't_frame'  : loadImg('images/map-setting/hangar/hangar-frm.png')
        }

        self.animations = {
            'player/run' : Animation(loadImgs('images/characters/boba-fett/run'), imgDuration=8),
            'player/idle': Animation([loadImg('images/characters/boba-fett/bobafett.png')], imgDuration=5),
            'player/jump': Animation([loadImg('images/crates/crate_blue.png')], imgDuration=5)
        }

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display = pygame.Surface((WIDTH / 2, HEIGHT / 2))
        self.clock = pygame.time.Clock()

        self.tilemap = Tilemap(self)

        self.player = Player(self, 'player', (WIDTH / 4, HEIGHT / 3), (23, 46))

        self.cameraOffset = [0, 0]
        

    def run(self):
        while True:
            self.display.blit(pygame.transform.scale_by(self.assets['bg_menu'], 0.5), (0, 0))

            self.cameraOffset[0] += (self.player.collisionRect().centerx - self.display.get_width() / 2 - self.cameraOffset[0]) / 20
            self.cameraOffset[1] += (self.player.collisionRect().centery - self.display.get_height() / 2 - self.cameraOffset[1]) / 20
            renderOffset = (int(self.cameraOffset[0]), int(self.cameraOffset[1]))

            self.tilemap.render(self.display, renderOffset)

            self.player.update(self.tilemap, ((self.player.pMov[1] - self.player.pMov[0]) * 4, 0))
            self.player.render(self.display, renderOffset)

            self.handleEvents()

            # self.display.blit(pygame.transform.scale_by(self.assets['t_frame'], 0.5), (0, 0))

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
                if event.key == pygame.K_SPACE:  
                    self.player.vel[1] = -4
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.player.notMovingLeft()
                if event.key == pygame.K_d:
                    self.player.notMovingRight()