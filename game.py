import pygame
import sys

from config import *
from entitity import Entity
from player import Player

from utils import loadImg, loadImgs

from level import Level
from animation import Animation
from gameobjects.weapons import Weapon


class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption(GAME_TITLE)

        self.assets = {
            'player'   : loadImg('images/characters/boba-fett/bobafett.png'),
            'crates'   : loadImgs('images/tiles/crates'),
            'grass'    : loadImgs('images/tiles/grass'),
            'platforms': loadImgs('images/tiles/platforms'),
        }

        self.bg_assets = {
            'bg_menu'  : loadImg('images/map-setting/hangar/hangar-bg.png'),
            'bg_smlp'  : loadImg('images/map-setting/hangar/hangar_bg_small.png'),
            'bg_smlj'  : loadImg('images/map-setting/hangar/hangar_bg_small.jpg')
        }

        self.animations = {
            'player/run'                  : Animation(loadImgs('images/characters/boba-fett/run'), imgDuration=8),
            'player/idle'                 : Animation([loadImg('images/characters/boba-fett/bobafett.png')], imgDuration=5),
            'player/jump'                 : Animation([loadImg('images/characters/boba-fett/run/2.png')], imgDuration=5),
            'player/wallslide'            : Animation([loadImg('images/characters/boba-fett/run/1.png')]),
            'player/run_weapon/e-11'      : Animation(loadImgs('images/characters/boba-fett/run_e11'), imgDuration=8),
            'player/idle_weapon/e-11'     : Animation([loadImg('images/characters/boba-fett/boba_e11.png')]),
            'player/jump_weapon/e-11'     : Animation([loadImg('images/characters/boba-fett/run_e11/2.png')], imgDuration=5),
            'player/wallslide_weapon/e-11': Animation([loadImg('images/characters/boba-fett/run_e11/1.png')], imgDuration=5),
            'weapon/e-11/idle'            : Animation([loadImg('images/weapons/e11.png')])
        }

        self.weaponAssets = {
            'weapon/e-11' : loadImg(WEAPONS['e-11']['path'])
        }

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display = pygame.Surface((WIDTH / 2, HEIGHT / 2))
        self.clock = pygame.time.Clock()

        self.level = Level(self, name='test', background='bg_smlj')
        self.level.load(f'{LEVELS_PATH}{self.level.name}.json')

        self.player : Player = Player(self, (100, 0), (18, 40))
        self.testWeapon : Weapon = Weapon(self, 'weapon/e-11', (200, 0), (34, 13))
        self.testWeapon.statsFromDict(WEAPONS['e-11'])

        self.cameraOffset = [0, 0]
        

    def run(self):
        while True:
            self.cameraOffset[0] += (self.player.collisionRect().centerx - self.display.get_width() / 2 - self.cameraOffset[0]) / 20
            self.cameraOffset[1] += (self.player.collisionRect().centery - self.display.get_height() / 2 - self.cameraOffset[1]) / 20
            renderOffset = (int(self.cameraOffset[0]), int(self.cameraOffset[1]))

            self.level.render(self.display, renderOffset, 0.5)

            self.player.update(self.level, ((self.player.pMov[1] - self.player.pMov[0]) * 4, 0))
            self.player.render(self.display, renderOffset)

            if not self.testWeapon.isPickedUp:
                self.testWeapon.update(self.level)
                self.testWeapon.render(self.display, renderOffset)

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
                    self.player.jump()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.player.notMovingLeft()
                if event.key == pygame.K_d:
                    self.player.notMovingRight()