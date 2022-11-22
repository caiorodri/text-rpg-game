from abc import ABC, abstractmethod
import os
from utils import clean, coloring_text, text_decorator
import json


class Character(ABC):

    def __init__(self, name: str, life: int, damage: int, shield: int, level: int, xp: float) -> None:

        self.name = name
        self.life = life
        self.damage = damage
        self.shield = shield
        self.level = level
        self.xp = xp

    @abstractmethod
    def show_stats(self, clean):

        pass

    @abstractmethod
    def check_stats(self):

        pass

class MainCharacter(Character):

    def __init__(self, name: str, user_class: str, life: int = 0, damage: int = 0, shield: int = 0, level: int = 0, xp: float = 0, stage: int = 0) -> None:
        
        super().__init__(name, life, damage, shield, level, xp)
        self.user_class = user_class

        with open('stats.json', 'r') as file:
            
            self.stats = json.load(file)
        
    def check_stats(self) -> None:

        user_level = f'level{self.level}'

        self.life = self.stats["leveis"][user_level][self.user_class]['vida']
        self.damage = self.stats["leveis"][user_level][self.user_class]['ataque']
        self.shield = self.stats["leveis"][user_level][self.user_class]['escudo']

    def check_level(self):

        with open('stats.json', 'r') as file:

            stats = json.load(file)

            for indice, _ in enumerate(stats["xp"]):
                
                if indice == 0:

                    pass

                elif self.xp < stats["xp"][f"level{indice+1}"] and self.xp >= stats["xp"][f"level{indice}"]:

                    self.level = indice

    def show_stats(self, clean_screen: bool = False):

        if clean_screen: clean()

        self.check_level()
        self.check_stats()

        text_decorator(f'{self.name}', 'cian')

        print(f'''| Classe: {self.user_class.title()}
| Level: {self.level}
| Xp: {self.xp}
|
| Vida: {self.life}
| Ataque: {self.damage}
| Escudo: {self.shield}
''')

    def level_up(self):

        old_level = self.level
        old_life = self.life
        old_damage = self.damage
        old_shield = self.shield

        self.check_level()
        self.check_stats()

        if old_level != self.level:

            print(f"""
{coloring_text(self.name, 'blue')}

Level Up

{coloring_text('Vida', 'green')} {old_life} -> {self.life} 
{coloring_text('Ataque', 'red')} {old_damage} -> {self.damage} 
{coloring_text('Escudo', 'yellow')} {old_shield} -> {self.shield} 
""")

class Monster(Character):

    def __init__(self, name: str, level: int, life: int = 0, damage: int = 0, shield: int = 0, xp: float = 0) -> None:
        super().__init__(name, life, damage, shield, level, xp)

        with open('monsters.json', 'r') as file:

            self.stats = json.load(file)

    def show_stats(self, clean_screen: bool = False):

        if clean_screen: clean()

        self.check_stats()
        
        text_decorator(self.name, 'red')

        print(f'''| Level: {self.level}
|
| Vida: {self.life}
| Ataque: {self.damage}
| Escudo: {self.shield}
''')

    def check_stats(self):

        monster_level = f'level{self.level}'

        self.life = self.stats["monstros"][f"{self.name.lower()}"][f"{monster_level}"]['vida']
        self.damage = self.stats["monstros"][f"{self.name.lower()}"][f"{monster_level}"]['ataque']
        self.shield = self.stats["monstros"][f"{self.name.lower()}"][f"{monster_level}"]['escudo']
        