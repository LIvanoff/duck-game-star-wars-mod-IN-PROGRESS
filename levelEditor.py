import pygame
import sys

from config import *

from utils import loadImg, loadImgs

from level import Level
from tile import Tile

RENDER_SCALE = 2.0

class Editor:
    '''
    L_CTRL - Режим сетки вкл/вкл \n
    R_CLICK - Удалить \n
    L_CLICK - Добавить \n 
    SCROLL - Переключение между типами ассетов \n 
    L_ALT + SCROLL - Переключение между ассетами в рамках выбранного типа \n
    O - Сохранить карту
    '''

    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption(EDITOR_TITLE)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display = pygame.Surface((int(WIDTH / 2), int(HEIGHT / 2)))
        self.clock = pygame.time.Clock()

        self.assets = {
            'crates'   : loadImgs('images/tiles/crates'),
            'grass'    : loadImgs('images/tiles/grass'),
            'platforms': loadImgs('images/tiles/platforms'),
        }
        self.bg_assets = {
            'bg_menu'  : loadImg('images/map-setting/hangar/hangar-bg.png'),
            'bg_smlp'  : loadImg('images/map-setting/hangar/hangar_bg_small.png'),
            'bg_smlj'  : loadImg('images/map-setting/hangar/hangar_bg_small.jpg')
        }
        print(self.assets)

        self.movement = [False, False, False, False]

        self.level = Level(self, name='test', background='bg_smlp')
        try:
            self.level.load(f'{LEVELS_PATH}{self.level.name}.json')
        except FileNotFoundError:
            pass    

        self.tiles = list(self.assets)
        self.tileClazzIdx = 0
        self.tileType = 0

        self.cameraOffset = [0, 0]

        self.clicking = False
        self.rightClicking = False
        self.alting = False

        self.ongrid = True
        

    def run(self):
        while True:
            self.display.fill((50, 50, 50))

            self.cameraOffset[0] += (self.movement[1] - self.movement[0]) * 2
            self.cameraOffset[1] += (self.movement[3] - self.movement[2]) * 2

            currentTileImg = self.assets[self.tiles[self.tileClazzIdx]][self.tileType].copy()
            currentTileImg.set_alpha(140)

            renderOffset = (int(self.cameraOffset[0]), int(self.cameraOffset[1]))
            self.level.render(self.display, renderOffset)

            self.mousePos = pygame.mouse.get_pos()
            self.mousePos = (self.mousePos[0]/RENDER_SCALE, self.mousePos[1]/RENDER_SCALE)
            actualTilePos = (int((self.mousePos[0] + self.cameraOffset[0]) // self.level.tileSize), int((self.mousePos[1] + self.cameraOffset[1]) // self.level.tileSize))

            # CURSOR
            if self.ongrid:
                self.display.blit(currentTileImg, (actualTilePos[0] * self.level.tileSize - self.cameraOffset[0], actualTilePos[1] * self.level.tileSize - self.cameraOffset[1]))
            else:
                self.display.blit(currentTileImg, self.mousePos)
            # ASSET DISPLAY
            self.display.blit(pygame.transform.scale2x(currentTileImg), (10, 10))
            
            if self.clicking and self.ongrid:
                self.level.onGridTilemap[f'{actualTilePos[0]}:{actualTilePos[1]}'] = Tile(clazz=self.tiles[self.tileClazzIdx], type=self.tileType, pos=actualTilePos)
            if self.rightClicking:
                deletingTileLocation = f'{actualTilePos[0]}:{actualTilePos[1]}'
                if deletingTileLocation in self.level.onGridTilemap:
                    del self.level.onGridTilemap[deletingTileLocation]
                for tile in self.level.offGridTilemap.copy():
                    offGridTileImg = self.assets[tile.clazz][tile.type]
                    offGridTileImgRect = pygame.Rect(tile.pos[0] - self.cameraOffset[0], tile.pos[1] - self.cameraOffset[1], offGridTileImg.get_width(), offGridTileImg.get_height())
                    if offGridTileImgRect.collidepoint(self.mousePos):
                        self.level.offGridTilemap.remove(tile)
 
            self.handleEvents()

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
                    self.clicking = True
                    if not self.ongrid:
                        self.level.offGridTilemap.append(Tile(clazz=self.tiles[self.tileClazzIdx], type=self.tileType, pos=(self.mousePos[0] + self.cameraOffset[0], self.mousePos[1] + self.cameraOffset[1])))
                if event.button == 3: 
                    self.rightClicking = True

                if self.alting:
                    if event.button == 4:
                        self.tileType = (self.tileType - 1) % len(self.assets[self.tiles[self.tileClazzIdx]])
                    if event.button == 5:
                        self.tileType = (self.tileType + 1) % len(self.assets[self.tiles[self.tileClazzIdx]])
                else: 
                    if event.button == 4:
                        self.tileClazzIdx = (self.tileClazzIdx - 1) % len(self.tiles)
                        self.tileType = 0
                    if event.button == 5:
                        self.tileClazzIdx = (self.tileClazzIdx + 1) % len(self.tiles)
                        self.tileType = 0
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.clicking = False
                if event.button == 3: 
                    self.rightClicking = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.movement[0] = True
                if event.key == pygame.K_d:
                    self.movement[1] = True
                if event.key == pygame.K_w: 
                    self.movement[2] = True
                if event.key == pygame.K_s:
                    self.movement[3] = True
                if event.key == pygame.K_t:
                    self.level.autotile()
                if event.key == pygame.K_o:
                    self.level.save(f'{LEVELS_PATH}{self.level.name}.json')
                if event.key == pygame.K_LALT:
                    self.alting = True
                if event.key == pygame.K_LCTRL:
                    self.ongrid = not self.ongrid
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.movement[0] = False
                if event.key == pygame.K_d:
                    self.movement[1] = False
                if event.key == pygame.K_w: 
                    self.movement[2] = False
                if event.key == pygame.K_s:
                    self.movement[3] = False
                if event.key == pygame.K_LALT:
                    self.alting = False


Editor().run()