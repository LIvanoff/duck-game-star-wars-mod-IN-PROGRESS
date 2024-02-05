

class Weapon:
    def __init__(self,
                 damage: int,
                 ammo_num: int,
                 path: str,
                 decay: float = None,
                 radius: int = None,
                 explosion_time: float = None
                 ):
        self.damage = damage
        self.ammo_num = ammo_num
        self.path = path
        self.decay = decay
        self.radius = radius
        self.explosion_time = explosion_time

