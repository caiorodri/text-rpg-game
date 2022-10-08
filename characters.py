from asyncio import shield


class Character:

    def __init__(self, name: str, life: int, damage: int, shield: int, level: int, xp: float) -> None:

        self.name = name
        self.life = life
        self.damage = damage
        self.shield = shield
        self.level = level
        self.xp = xp


class MainCharacter(Character):

    def __init__(self, name: str, life: int, damage: int, shield: int, level: int, xp: float, user_class: str) -> None:
        
        super().__init__(name, life, damage, shield, level, xp)
        self.xp = xp
        self.user_class = user_class

    def check_stats(self):

        user_level = f'level{self.level}'



class Monster(Character):

    def __init__(self, name: str, life: int, shield: int, damage: int, level: int, xp: float) -> None:
        super().__init__(name, life, damage, shield, level, xp)

