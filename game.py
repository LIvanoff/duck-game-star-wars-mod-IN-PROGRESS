import pygame
import sys

from config import *
from entitity import Entity
from player import Player

from utils import loadImg, loadImgs, loadSound

from level import Level
from animation import Animation
from gameobjects.weapons import Weapon
from gameobjects.grenade import Grenade
from gameobjects.projectile import Projectile
from gameobjects.weaponwithprojectile import WeaponWithProjectile
from config import WEAPONS


class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption(GAME_TITLE)
        pygame.display.set_icon(loadImg('images/icon/icon.png'))

        self.assets = {
            'player': loadImg('images/characters/boba-fett/bobafett.png'),
            'crates': loadImgs('images/tiles/crates'),
            'grass': loadImgs('images/tiles/grass'),
            'platforms': loadImgs('images/tiles/platforms'),
        }

        self.bg_assets = {
            'bg_menu': loadImg('images/map-setting/hangar/hangar-bg.png'),
            'bg_smlp': loadImg('images/map-setting/hangar/hangar_bg_small.png'),
            'bg_smlj': loadImg('images/map-setting/hangar/hangar_bg_small.jpg')
        }

        self.animations = {
            'player/run': Animation(loadImgs('images/characters/boba-fett/run'), imgDuration=8),
            'player/idle': Animation([loadImg('images/characters/boba-fett/bobafett.png')], imgDuration=5),
            'player/jump': Animation([loadImg('images/characters/boba-fett/run/2.png')], imgDuration=5),
            'player/wallslide': Animation([loadImg('images/characters/boba-fett/run/1.png')]),
            
            'weapon/e-11/idle': Animation([loadImg('images/weapons/e11.png')]),
            'player/run_weapon/e-11': Animation(loadImgs('images/characters/boba-fett/run_e11'), imgDuration=8),
            'player/idle_weapon/e-11': Animation([loadImg('images/characters/boba-fett/boba_e11.png')]),
            'player/jump_weapon/e-11': Animation([loadImg('images/characters/boba-fett/run_e11/2.png')], imgDuration=5),
            'player/wallslide_weapon/e-11': Animation([loadImg('images/characters/boba-fett/run_e11/1.png')],imgDuration=5),

            'grenade/thermal_imploder/idle': Animation([loadImg('images/weapons/thermal_imploder.png')]),
            'player/run_grenade/thermal_imploder': Animation(loadImgs('images/characters/boba-fett/run_thermal_imploder'), imgDuration=8),
            'player/jump_grenade/thermal_imploder': Animation([loadImg('images/characters/boba-fett/run_thermal_imploder/2.png')], imgDuration=5),
            'player/idle_grenade/thermal_imploder': Animation([loadImg('images/characters/boba-fett/boba_thermal_imploder.png')]),

            'projectile_red/idle': Animation([loadImg('images/shots/shot_red.png')]),
            'projectile_grenade/thermal_imploder/idle': Animation([loadImg('images/weapons/thermal_imploder.png')]),
        }

        self.sounds = {
            'menu': loadSound('sounds/menu/main_theme.mp3'),
            'weapon/e-11/shoot' : loadSound('sounds/weapons/e11.mp3'),
            'grenade/thermal_imploder/shoot' : loadSound('sounds/weapons/e11.mp3'),
            'weapon/cocking': loadSound('sounds/weapons/cocking1.mp3'),
            'projectile_grenade/thermal_imploder/explode': loadSound('sounds/weapons/thermal_imploder.mp3')
        }

        self.weapons : list[Weapon] = [
            Grenade(self, "grenade/thermal_imploder", (200, 0), WEAPONS['thermal imploder']['imgsize'], WEAPONS['thermal imploder']),
            WeaponWithProjectile(self, 'weapon/e-11', (300, 0), (34, 13), WEAPONS['e-11'])
        ]

        self.projectiles : list[Projectile] = []
        
        if IS_FULLSCREEN:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.screenWidth = self.screen.get_width()
            self.screenHeight = self.screen.get_height()
        else: 
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
            self.screenHeight = HEIGHT
            self.screenWidth = WIDTH

        self.display = pygame.Surface((self.screenWidth / 2, self.screenHeight / 2))
        self.clock = pygame.time.Clock()

        if MUSIC_ENABLED:
            self.sounds['menu'].play(-1)

        self.level = Level(self, name='test', background='bg_smlj')
        self.level.load(f'{LEVELS_PATH}{self.level.name}.json')

        self.player: Player = Player(self, (100, 0), (18, 40))

        self.cameraOffset = [0, 0]


    def run(self):
        grenade_group = pygame.sprite.Group()
        while True:

            grenade_group.update()
            grenade_group.draw(self.display)

            self.cameraOffset[0] += (self.player.collisionRect().centerx - self.display.get_width() / 2 -
                                     self.cameraOffset[0]) / 20
            self.cameraOffset[1] += (self.player.collisionRect().centery - self.display.get_height() / 2 -
                                     self.cameraOffset[1]) / 20
            renderOffset = (int(self.cameraOffset[0]), int(self.cameraOffset[1]))

            self.level.render(self.display, renderOffset, 0.5)

            self.player.update(self.level, ((self.player.pMov[1] - self.player.pMov[0]) * 4, 0))
            self.player.render(self.display, renderOffset)


            for weapon in self.weapons:
                if not weapon.isPickedUp:
                    weapon.update(self.level)
                    weapon.render(self.display, renderOffset)


            for projectile in self.projectiles:
                projectile.update(self.level)
                projectile.render(self.display, renderOffset)
                
            self.removeDeadProjectiles()

            # if self.testWeapon.isThrow and not self.testWeapon.isBlowup:
            #     print('is throw')
            #     self.testWeapon.throw(self.player.direction)
            #     self.grenade = False

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.player.currentWeapon:
                        self.player.currentWeapon.shoot()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.isMovingLeft()
                if event.key == pygame.K_d:
                    self.player.isMovingRight()
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                if event.key == pygame.K_q:
                    if self.player.currentWeapon:
                        self.player.currentWeapon.drop()
                if event.key == pygame.K_z:
                    self.player.dash()
                    # self.testWeapon.isThrow = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.player.notMovingLeft()
                if event.key == pygame.K_d:
                    self.player.notMovingRight()

    def clean(self):
        self.removeDeadProjectiles()
        self.removeThrownGrenades()

    def removeDeadProjectiles(self):
        self.projectiles = [x for x in self.projectiles if not x.dead]

    def removeThrownGrenades(self):
        pass