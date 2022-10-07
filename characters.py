class Character:

    def __init__(self, name: str, life: int, damage: int, level: int) -> None:

        self.name = name
        self.life = life
        self.damage = damage
        self.level = level


class MainCharacter(Character):

    def __init__(self, name: str, life: int, damage: int, shield: int, level: int, xp: float, user_class: str) -> None:
        
        super().__init__(name, life, level, damage)
        self.xp = xp
        self.user_class = user_class


class Monster(Character):

    def __init__(self, name: str, life: int, damage: int, level: int) -> None:
        super().__init__(name, life, damage, level)

