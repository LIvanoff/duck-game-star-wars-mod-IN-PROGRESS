GAME_TITLE : str = "Some crappy game"
EDITOR_TITLE : str = "Level Editor"

CLOCK_TICKSPEED : int = 165

WIDTH = 1920
HEIGHT = 1080

ASSETS_PATH = 'assets/'


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
    'dlt-19': {
        'damage': 100,
        'ammo_num': 3,
        'decay': 1.5,
        'path': 'assets/images/weapons/dlt-19.png'
    },
    'e-11': {
        'damage': 30,
        'ammo_num': 20,
        'decay': 0.2,
        # 'overheating_time': ,
        'path': 'assets/images/weapons/e-11.png'},
    'dl-44': {
        'damage': 50,
        'ammo_num': 10,
        'decay': 0.7,
        'path': 'assets/images/weapons/dl-44.png'},
    'sonic imploder': {
        'damage': 100,
        'radius': 20,
        'explosion_time': 3.5,
        'path': 'assets/images/weapons/sonic-imploder.png'}
}


# PLAYER PROPS
JUMP_STRENGTH = 5