from asyncio import shield
import json


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
        self.user_class = user_class

    def check_stats(self) -> None:

        user_level = f'level{self.level}'

        with open('stats.json', 'r') as file:

            stats = json.load(file)

            self.life = stats["leveis"][user_level][self.user_class]['vida']
            self.damage = stats["leveis"][user_level][self.user_class]['ataque']
            self.shield = stats["leveis"][user_level][self.user_class]['escudo']

    def check_level(self):

        pass

class Monster(Character):

    def __init__(self, name: str, life: int, shield: int, damage: int, level: int, xp: float) -> None:
        super().__init__(name, life, damage, shield, level, xp)

