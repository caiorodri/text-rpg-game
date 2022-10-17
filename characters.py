from abc import ABC, abstractmethod
from utils import coloring_text
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
    def show_stats(self):

        pass

    @abstractmethod
    def check_stats(self):

        pass

class MainCharacter(Character):

    def __init__(self, name: str, life: int, damage: int, shield: int, level: int, xp: float, user_class: str) -> None:
        
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

    def show_stats(self):

        self.check_level()
        self.check_stats()

        print(f'''
| \033[1;36m{self.name}\033[m
|
| Classe: {self.user_class.title()}
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

    def show_stats(self):

        self.check_stats()
        
        print(f'''
| \033[1;31m{self.name}\033[m
|
| Level: {self.level}
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
        

main_character = MainCharacter('User', 0, 0, 0, 0, 0, 'arqueiro')

skeleton = Monster('Esqueleto', 1)

main_character.show_stats()
print('---------------------')
skeleton.show_stats()
