from abc import ABC, abstractmethod
import sqlite3
from utils import animated_text, clean, text_decorator
import json


class Character(ABC):

    def __init__(self, name: str, life: int, damage: int, shield: int, level: int, xp: int, gold: int) -> None:

        self.name = name
        self.life = life
        self.damage = damage
        self.shield = shield
        self.level = level
        self.xp = xp
        self.gold = gold

    @abstractmethod
    def show_stats(self, clean):

        pass

    @abstractmethod
    def check_stats(self):

        pass

class MainCharacter(Character):

    def __init__(self, name: str, user_class: str, life: int = 0, damage: int = 0, shield: int = 0, level: int = 1, xp: int = 0, gold: int = 0, dungeon: int = 1, floor: int = 1, deaths: int = 0, life_increase: float = 0, damage_increase: float = 0, shield_increase: float = 0, gold_increase: float = 0, xp_increase: float = 0, dodge: float = 0, critical_chance: float = False, critical_damage: float = False) -> None:
        
        super().__init__(name, life, damage, shield, level, xp, gold)
        self.user_class = user_class
        self.dungeon = dungeon
        self.floor = floor
        self.deaths = deaths
        self.life_increase = life_increase
        self.damage_increase = damage_increase
        self.shield_increase = shield_increase
        self.gold_increase = gold_increase
        self.xp_increase = xp_increase
        self.dodge = dodge
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage

        with open('stats.json', 'r') as file:
            
            self.stats = json.load(file)
        
    def check_stats(self) -> None:

        user_level = f'level{self.level}'

        self.life = self.stats["leveis"][user_level][self.user_class]['vida']
        self.damage = self.stats["leveis"][user_level][self.user_class]['ataque']
        self.shield = self.stats["leveis"][user_level][self.user_class]['escudo']

        self.life += round(self.life * self.life_increase)
        self.damage += round(self.damage * self.damage_increase)
        self.shield += round(self.shield * self.shield_increase)

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

        text_decorator(f" {self.name}'s Stats ", 'cian')

        print(f'''| Classe: {self.user_class.title()}
| Level: \033[1;34m{self.level}\033[m
| Xp: \033[1;36m{self.xp}\033[m
| Gold: \033[1;33m{self.gold}\033[m G
|
| Vida: \033[1;32m{self.life}\033[m
| Ataque: \033[1;36m{self.damage}\033[m
| Escudo: \033[1;33m{self.shield}\033[m
|
| Aumento de Vida: \033[1;32m{int(self.life_increase * 100)}\033[m %
| Aumento de Ataque: \033[1;36m{int(self.damage_increase * 100)}\033[m %
| Aumento de Escudo: \033[1;33m{int(self.shield_increase * 100)}\033[m %
|
| Aumento de Xp: \033[1;36m{int(self.xp_increase * 100)}\033[m %
| Aumento de Gold: \033[1;33m{int(self.gold_increase * 100)}\033[m %
|
| Chance de Desviar: \033[1;33m{self.dodge}\033[m %
| Chance de Crítico: \033[1;31m{self.critical_chance}\033[m %
| Dano Crítico: \033[1;31m{100 + int(self.critical_damage * 100)}\033[m %
|
| Dungeon {self.dungeon}
| Andar {self.floor}
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
            
            animated_text(f"Level \033[1;34m{old_level}\033[m  ->  Level \033[1;34m{self.level}\033[m", 0.035)

            print('\n')

            animated_text(f"\033[1;32m{old_life}\033[m HP  ->  \033[1;32m{self.life}\033[m HP", 0.035)

            print()
                        
            animated_text(f'\033[1;36m{old_damage}\033[m ATK  ->  \033[1;36m{self.damage}\033[m ATK', 0.035)
            
            print()
            
            animated_text(f'\033[1;33m{old_shield}\033[m DEF  ->  \033[1;33m{self.shield}\033[m DEF', 0.035)

            animated_text(input('\n\n\033[1;33mPresisone enter para continuar...\033[m'))

    def update_stats(self):

        connection = sqlite3.connect('user.db')
        cursor = connection.cursor()

        cursor.execute(f"UPDATE users SET user_level = '{self.level}', user_class = '{self.user_class}', user_xp = '{self.xp}', user_gold = '{self.gold}', user_dungeon = '{self.dungeon}', user_floor = '{self.floor}', deaths = '{self.deaths}', user_floor = '{self.floor}', gold_increase = '{self.gold_increase}', xp_increase = '{self.xp_increase}', dodge = '{self.dodge}' WHERE username = '{self.name}'")

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

    def change_class(self):

        valid = False
        user_class = ''

        while True:

            text_decorator('Mudança de Classe')

            animated_text('Você perderá tudo que conquistou até aqui (Level, XP, Ouro, etc...)')
            animated_text('\nE voltará para a primeira Dungeon!')

            animated_text('\nTem certeza que deseja mudar de classe?')
            
            animated_text('''\n 
[0] Não, Eu não quero mudar de classe
[1] Sim, Eu quero mudar de classe

\033[1;33mEscolha do Usuário: \033[m''')

            user_choice = input('')

            if user_choice == '0' or user_choice == 'não, eu não quero mudar de classe':

                return

            elif user_choice == '1':

                text_decorator('Mudança de Classe')

                print('''Escolha uma classe para trocar

[0] Sair

[1] Guerreiro
[2] Arqueiro
[3] Mago
''')

                while not valid:

                    user_class = input('Escolha do Usuário: ').strip().lower()

                    if user_class == 'guerreiro' or user_class == '1':

                        user_class = 'guerreiro'
                        valid = True

                    elif user_class == 'arqueiro' or user_class == '2':
                        
                        user_class = 'arqueiro'
                        valid = True
                
                    elif user_class == 'mago' or user_class == '3':

                        user_class = 'mago'
                        valid = True

                    elif user_class == 'sair' or user_class == '0':

                        return

                    else: print('\nEscolha inválida!\n')
                
                self.user_class = user_class
                self.gold = 0
                self.xp = 0
                self.dungeon = 0
                self.floor = 0

                self.update_stats()
                return

class Monster(Character):

    def __init__(self, name: str, level: int, life: int = 0, damage: int = 0, shield: int = 0, xp: int = 0, gold: int = 0, boss: bool = False) -> None:
        super().__init__(name, life, damage, shield, level, xp, gold)

        self.boss = boss

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

        if self.boss:

            print(f'| Level: Boss', end='')    

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

        self.life = self.stats["monstros"][f"{monster_level}"][f"{self.name.lower()}"]['vida']
        self.damage = self.stats["monstros"][f"{monster_level}"][f"{self.name.lower()}"]['ataque']
        self.shield = self.stats["monstros"][f"{monster_level}"][f"{self.name.lower()}"]['escudo']
        self.xp = self.stats["monstros"][f"{monster_level}"][f"{self.name.lower()}"]['xp']
        self.gold = self.stats["monstros"][f"{monster_level}"][f"{self.name.lower()}"]['gold']

        if self.boss:

            self.damage *= 3
            self.life *= 3
            self.shield *= 3
            self.xp *= 5
            self.gold *= 5
