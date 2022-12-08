from abc import ABC, abstractmethod
import sqlite3
from utils import animated_text, clean, text_decorator
import json


class Character(ABC):

    def __init__(self, name: str, life: int, damage: int, shield: int, level: int, xp: int) -> None:

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

    def __init__(self, name: str, user_class: str, life: int = 0, damage: int = 0, shield: int = 0, level: int = 1, xp: int = 0, dungeon: int = 1, floor: int = 1, deaths: int = 0) -> None:
        
        super().__init__(name, life, damage, shield, level, xp)
        self.user_class = user_class
        self.dungeon = dungeon
        self.floor = floor
        self.deaths = deaths

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

        text_decorator(f"{self.name}'s Stats", 'cian')

        print(f'''| Classe: {self.user_class.title()}
| Level: \033[1;34m{self.level}\033[m
| Xp: {self.xp}
|
| Vida: \033[1;32m{self.life}\033[m
| Ataque: \033[1;36m{self.damage}\033[m
| Escudo: \033[1;33m{self.shield}\033[m
|
| Dungeon {self.dungeon}
''')

    def level_up(self) -> None:

        self.check_stats()

        old_level = self.level
        old_life = self.life
        old_damage = self.damage
        old_shield = self.shield

        self.check_level()
        self.check_stats()

        if old_level != self.level:

            text_decorator('Level UP', 'cian')
            
            animated_text(f"Level \033[1;34m{old_level}\033[m  ->  Level \033[1;34m{self.level}\033[m")

            animated_text(f"\033[1;32m{old_life}\033[m HP  ->  \033[1;32m{self.life}\033[m HP")

            print()
                        
            animated_text(f'\033[1;36m{old_damage}\033[m ATK  ->  \033[1;36m{self.damage}\033[m ATK')
            
            print()
            
            animated_text(f'\033[1;33m{old_shield}\033[m DEF  ->  \033[1;33m{self.shield}\033[m DEF')

            animated_text(input('\n\n\033[1;33mPresisone enter para continuar...\033[m'))

    def update_stats(self):

        connection = sqlite3.connect('user.db')
        cursor = connection.cursor()

        cursor.execute(f"UPDATE users SET user_level = '{self.level}', user_xp = '{self.xp}', user_dungeon = '{self.dungeon}', deaths = '{self.deaths}', user_floor = '{self.floor}' WHERE username = '{self.name}'")

        connection.commit()
        cursor.close()
        connection.close()

    def update_deaths(self):

        connection = sqlite3.connect('user.db')
        cursor = connection.cursor()

        cursor.execute(f"UPDATE users SET deaths = '{self.deaths}' WHERE username = '{self.name}'")

        connection.commit()
        cursor.close()
        connection.close()

class Monster(Character):

    def __init__(self, name: str, level: int, life: int = 0, damage: int = 0, shield: int = 0, xp: int = 0, boss: bool = False) -> None:
        super().__init__(name, life, damage, shield, level, xp)

        if boss:

            self.damage *= 3
            self.life *= 3
            self.shield *= 3
            self.xp *= 5

        with open('monsters.json', 'r') as file:

            self.stats = json.load(file)

    def show_stats(self, clean_screen: bool = False):

        if clean_screen: clean()

        self.check_stats()
        
        text_decorator(self.name, 'red')

        
        if self.level == 0:

            print(f'| Level: {self.level}', end='')    

        else:

            print(f'| Level: {self.level}', end='')
        
        print(f'''
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
        self.xp = self.stats["monstros"][f"{self.name.lower()}"][f"{monster_level}"]['xp']
        