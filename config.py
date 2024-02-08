GAME_TITLE : str = "Some crappy game"
EDITOR_TITLE : str = "Level Editor"

CLOCK_TICKSPEED : int = 60

# WIDTH = 1920
# HEIGHT = 1080

WIDTH = 960
HEIGHT = 540

ASSETS_PATH = 'assets/'
LEVELS_PATH = 'levels/'

DEFAULT_TILESIZE = 21

LOCATION = [
    'hangar',
    'hoth',
    'mustafar',
    'bespin',
    'tattoine'
]

ROUNDS = 5

WEAPONS = {
    'dlt-19d': {
        'name': 'dlt-19d',
        'damage': 100,
        'ammo_num': 3,
        'decay': 1.5,
        'img_path': 'images/weapons/dlt19d.png',
        'shot_sound_path': 'assets/sounds/weapons/dlt19.mp3'
    },
    'e-11': {
        'name': 'e-11',
        'damage': 30,
        'ammo_num': 20,
        'decay': 0.2,
        # 'overheating_time': 2,
        'img_path': 'images/weapons/e11.png',
        'shot_sound_path': 'assets/sounds/weapons/e11.mp3'
    },
    'dl-44': {
        'name': 'dl-44',
        'damage': 50,
        'ammo_num': 10,
        'decay': 0.7,
        'img_path': 'images/weapons/dl44.png',
        'shot_sound_path': 'assets/sounds/weapons/dl44.mp3'},
    'dlt-44': {
        'name': 'dlt-19d',
        'damage': 33,
        'ammo_num': 100,
        'decay': 0.5,
        'img_path': 'images/weapons/dlt19d.png',
        'shot_sound_path': 'assets/sounds/weapons/dlt19.mp3'
    },
    'sonic imploder': {
        'name': 'sonic imploder',
        'damage': 100,
        'radius': 200,
        'explosion_time': 40.5,
        'img_path': 'images/weapons/sonic_imploder.png',
        'imgsize': (7, 13),
        'shot_sound_path': '',
        'explosion_sound_path': 'assets/sounds/weapons/thermal_imploder.mp3'},
    'thermal imploder': {
        'name': 'thermal imploder',
        'damage': 100,
        'ammo_num': 1,
        'decay': 0.0,
        'radius': 300,
        'explosion_time': 40.,
        'img_path': 'images/weapons/thermal_imploder.png',
        'imgsize': (7, 13),
        'shot_sound_path': '',
        'explosion_sound_path': 'assets/sounds/weapons/thermal_imploder.mp3'}
}

# PLAYER PROPS
JUMP_STRENGTH = 4
MAX_JUMPS = 1