from weapons import Weapon


class WeaponThrowable(Weapon):
    def __init__(self, game, type: str, pos: tuple, size: tuple, damage: int = 10, decay: int = 10, ammo_num: int = 100) -> None:
        super().__init__(game, type, pos, size, damage, decay, ammo_num)


    