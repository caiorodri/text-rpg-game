from abc import ABC, ABCMeta, abstractmethod
from typing import List
from characters import MainCharacter
import sqlite3

class Blessing(ABC):

    def __init__(self, name: str, description: str, next_description: str, level: int, gold: int) -> None:
        
        self.name = name
        self.description = description
        self.next_description = next_description
        self.level = level
        self.gold = gold
    
    @abstractmethod
    def effect(self, user: MainCharacter, active: bool = False) -> None:

        pass

    @abstractmethod
    def register(self, user: MainCharacter, active: bool = False) -> None:

        if active:

            self.effect(user, True)
        
        else:

            self.effect(user)

        connection = sqlite3.connect('user.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM shop WHERE name = '{self.name}'")

        item = cursor.fetchall()

        if len(item) == 1:

            self.effect(user)

            cursor.execute(f"UPDATE shop SET gold = '{self.gold}', description = '{self.description}', next_description = '{self.next_description}' WHERE name = '{self.name}'")
        
        else:

            cursor.execute(f"INSERT INTO shop ('name', 'description', 'next_description', 'gold') VALUES ('{self.name}', '{self.description}', '{self.next_description}', '{self.gold}')")
        
        connection.commit()
        cursor.close()
        connection.close()

class LifeGoddessBlessing(Blessing):

    def __init__(self, name: str = '', description: str = '', next_description: str = '', gold: int = 200, level: int = 0) -> None:
        super().__init__(name, description, next_description, level, gold)

        self.name = 'Goddess of Life'
        self.next_description = f'"{self.name}" concede ao usuário um aumento de 10% na vida total'

    def effect(self, user: MainCharacter) -> None:
        
        user.life_increase = 0

        if self.level == 1:

            user.life_increase += 0.10

            self.gold = 350

            self.description = f'"{self.name}" concede ao usuário um aumento de 10% na vida total'
            self.next_description = f'"{self.name} II" concede ao usuário um aumento de 15% na vida total'

        elif self.level == 2:

            user.life_increase += 0.15

            self.gold = 500

            self.description = f'"{self.name} II" concede ao usuário um aumento de 15% na vida total'
            self.next_description = f'"{self.name} III" concede ao usuário um aumento de 20% na vida total'

        elif self.level == 3:

            user.life_increase += 0.20

            self.gold = 750

            self.description = f'"{self.name} III" concede ao usuário um aumento de 20% na vida total'
            self.next_description = f'"{self.name} IV" concede ao usuário um aumento de 25% na vida total'

        elif self.level == 4:

            user.life_increase += 0.25

            self.gold = 1000

            self.description = f'"{self.name} IV" concede ao usuário um aumento de 25% na vida total'
            self.next_description = f'"{self.name} V" concede ao usuário um aumento de 30% na vida total'

        elif self.level == 5:

            user.life_increase += 0.30

            self.description = f'"{self.name} V" concede ao usuário um aumento de 30% na vida total'

    def register(self, user: MainCharacter, active: bool = False) -> None:
        return super().register(user, active)

class WarGodBlessing(Blessing):

    def __init__(self, name: str = '', description: str = '', next_description: str = '', gold: int = 300, level: int = 0) -> None:
        super().__init__(name, description, next_description, level, gold)

        self.name = 'God of War'
        self.next_description = f'"{self.name}" concede ao usuário um aumento de 10% no ataque'

    def effect(self, user: MainCharacter) -> None:
        
        user.damage_increase = 0

        if self.level == 1:

            user.damage_increase += 0.10

            self.gold = 500

            self.description = f'"{self.name}" concede ao usuário um aumento de 10% no ataque'
            self.next_description = f'"{self.name} II" concede ao usuário um aumento de 15% no ataque'

        elif self.level == 2:

            user.damage_increase += 0.15

            self.gold = 800

            self.description = f'"{self.name} II" concede ao usuário um aumento de 15% no ataque'
            self.next_description = f'"{self.name} III" concede ao usuário um aumento de 20% no ataque'

        elif self.level == 3:

            user.damage_increase += 0.20

            self.gold = 1200

            self.description = f'"{self.name} III" concede ao usuário um aumento de 20% no ataque'
            self.next_description = f'"{self.name} IV" concede ao usuário um aumento de 25% no ataque'

        elif self.level == 4:

            user.damage_increase += 0.25

            self.gold = 1500

            self.description = f'"{self.name} IV" concede ao usuário um aumento de 25% no ataque'
            self.next_description = f'"{self.name} V" concede ao usuário um aumento de 30% no ataque'

        elif self.level == 5:

            user.damage_increase += 0.30

            self.description = f'"{self.name} V" concede ao usuário um aumento de 30% no ataque'

    def register(self, user: MainCharacter, active: bool = False) -> None:
        return super().register(user, active)

class IronHeart(Blessing):

    def __init__(self, name: str = '', description: str = '', next_description: str = '', gold: int = 250, level: int = 0) -> None:
        super().__init__(name, description, next_description, level, gold)

        self.name = 'Iron Heart'
        self.next_description = f'"{self.name}" concede ao usuário um aumento de 10% na defesa'

    def effect(self, user: MainCharacter) -> None:
        
        user.shield_increase = 0

        if self.level == 1:

            user.shield_increase += 0.10

            self.gold = 400

            self.description = f'"{self.name}" concede ao usuário um aumento de 10% na defesa'
            self.next_description = f'"{self.name} II" concede ao usuário um aumento de 15% na defesa'

        elif self.level == 2:

            user.shield_increase += 0.15

            self.gold = 650

            self.description = f'"{self.name} II" concede ao usuário um aumento de 15% na defesa'
            self.next_description = f'"{self.name} III" concede ao usuário um aumento de 20% na defesa'

        elif self.level == 3:

            user.shield_increase += 0.20

            self.gold = 900

            self.description = f'"{self.name} III" concede ao usuário um aumento de 20% na defesa'
            self.next_description = f'"{self.name} IV" concede ao usuário um aumento de 25% na defesa'

        elif self.level == 4:

            user.shield_increase += 0.25

            self.gold = 1200

            self.description = f'"{self.name} IV" concede ao usuário um aumento de 25% na defesa'
            self.next_description = f'"{self.name} V" concede ao usuário um aumento de 30% na defesa'

        elif self.level == 5:

            user.shield_increase += 0.30

            self.description = f'"{self.name} V" concede ao usuário um aumento de 30% na defesa'

    def register(self, user: MainCharacter, active: bool = False) -> None:
        return super().register(user, active)

class Greed(Blessing):

    def __init__(self, name: str = '', description: str = '', next_description: str = '', gold: int = 500, level: int = 0) -> None:
        super().__init__(name, description, next_description , level, gold)

        self.name = 'Greed'
        self.next_description = f'"{self.name}" concede ao usuário um aumento de 10% no ouro em batalhas'

    def effect(self, user: MainCharacter) -> None:

        user.gold_increase = 0

        if self.level == 1:

            user.gold_increase += 0.10

            self.gold = 400

            self.description = f'"{self.name}" concede ao usuário um aumento de 10% no ouro em batalhas'
            self.next_description = f'"{self.name} II" concede ao usuário um aumento de 15% no ouro em batalhas'

        elif self.level == 2:

            user.gold_increase += 0.15

            self.gold = 650

            self.description = f'"{self.name} II" concede ao usuário um aumento de 15% no ouro em batalhas'
            self.next_description = f'"{self.name} III" concede ao usuário um aumento de 20% no ouro em batalhas'

        elif self.level == 3:

            user.gold_increase += 0.20

            self.gold = 900

            self.description = f'"{self.name} III" concede ao usuário um aumento de 20% no ouro em batalhas'
            self.next_description = f'"{self.name} IV" concede ao usuário um aumento de 25% no ouro em batalhas'

        elif self.level == 4:

            user.gold_increase += 0.25

            self.gold = 1200

            self.description = f'"{self.name} IV" concede ao usuário um aumento de 25% no ouro em batalhas'
            self.next_description = f'"{self.name} V" concede ao usuário um aumento de 30% no ouro em batalhas'

        elif self.level == 5:

            user.gold_increase += 0.30

            self.description = f'"{self.name} V" concede ao usuário um aumento de 30% no ouro em batalhas'

    def register(self, user: MainCharacter, active: bool = False) -> None:
        return super().register(user, active)

class Wisdom(Blessing):

    def __init__(self, name: str = '', description: str = '', next_description: str = '', gold: int = 500, level: int = 0) -> None:
        super().__init__(name, description, next_description, level, gold)
        
        self.name = 'Wisdom'
        self.next_description = f'"{self.name}" concede ao usuário um aumento de 20% no xp em batalhas'

    def effect(self, user: MainCharacter) -> None:
        
        user.xp_increase = 0

        if self.level == 1:

            user.xp_increase += 0.10

            self.gold = 400

            self.description = f'"{self.name}" concede ao usuário um aumento de 20% no xp em batalhas'
            self.next_description = f'"{self.name} II" concede ao usuário um aumento de 25% no xp em batalhas'

        elif self.level == 2:

            user.xp_increase += 0.15

            self.gold = 650

            self.description = f'"{self.name} II" concede ao usuário um aumento de 25% no xp em batalhas'
            self.next_description = f'"{self.name} III" concede ao usuário um aumento de 30% no xp em batalhas'

        elif self.level == 3:

            user.xp_increase += 0.20

            self.gold = 900

            self.description = f'"{self.name} III" concede ao usuário um aumento de 30% no xp em batalhas'
            self.next_description = f'"{self.name} IV" concede ao usuário um aumento de 35% no xp em batalhas'

        elif self.level == 4:

            user.xp_increase += 0.25

            self.gold = 1200

            self.description = f'"{self.name} IV" concede ao usuário um aumento de 35% no xp em batalhas'
            self.next_description = f'"{self.name} V" concede ao usuário um aumento de 40% no xp em batalhas'

        elif self.level == 5:

            user.xp_increase += 0.30

            self.description = f'"{self.name} V" concede ao usuário um aumento de 40% no xp em batalhas'

    def register(self, user: MainCharacter, active: bool = False) -> None:
        return super().register(user, active)

class Dodge(Blessing):

    def __init__(self, name: str = '', description: str = '', next_description: str = '', gold: int = 800, level: int = 0) -> None:
        super().__init__(name, description, next_description, level, gold)
        
        self.name = 'Dodge'
        self.next_description = f'"{self.name}" concede ao usuário 1% de chance de esquivar de ataques'

    def effect(self, user: MainCharacter) -> None:

        user.dodge = 0

        if self.level == 1:

            user.dodge += 1

            self.gold = 1000

            self.description = f'"{self.name}" concede ao usuário 1% de chance de esquivar de ataques'
            self.next_description = f'"{self.name} II" concede ao usuário 2% de chance de esquivar de ataques'

        elif self.level == 2:

            user.dodge += 2

            self.gold = 1250

            self.description = f'"{self.name} II" concede ao usuário 2% de chance de esquivar de ataques'
            self.next_description = f'"{self.name} III" concede ao usuário 3% de chance de esquivar de ataques'

        elif self.level == 3:

            user.dodge += 3

            self.gold = 1400

            self.description = f'"{self.name} III" concede ao usuário 3% de chance de esquivar de ataques'
            self.next_description = f'"{self.name} IV" concede ao usuário 4% de chance de esquivar de ataques'

        elif self.level == 4:

            user.dodge += 4

            self.gold = 1650

            self.description = f'"{self.name} IV" concede ao usuário 4% de chance de esquivar de ataques'
            self.next_description = f'"{self.name} V" concede ao usuário 5% de chance de esquivar de ataques'

        elif self.level == 5:

            user.dodge += 5

            self.description = f'"{self.name} V" concede ao usuário 5% de chance de esquivar de ataques'

    def register(self, user: MainCharacter, active: bool = False) -> None:
        return super().register(user, active)

class CriticalChance(Blessing):

    def __init__(self, name: str = '', description: str = '', next_description: str = '', gold: int = 1000, level: int = 0) -> None:
        super().__init__(name, description, next_description, level, gold)
        
        self.name = 'Critical Chance'
        self.next_description = f'"{self.name}" concede ao usuário 2% de chance de dano critico'

    def effect(self, user: MainCharacter) -> None:

        user.critical_chance = 0

        if self.level == 1:

            user.critical_chance += 2

            self.gold = 1000

            self.description = f'"{self.name}" concede ao usuário 2% de chance de dano critico'
            self.next_description = f'"{self.name} II" concede ao usuário 3% de chance de dano critico'

        elif self.level == 2:

            user.critical_chance += 3

            self.gold = 1500

            self.description = f'"{self.name} II" concede ao usuário 3% de chance de dano critico'
            self.next_description = f'"{self.name} III" concede ao usuário 4% de chance de dano critico'

        elif self.level == 3:

            user.critical_chance += 4

            self.gold = 2000

            self.description = f'"{self.name} III" concede ao usuário 4% de chance de dano critico'
            self.next_description = f'"{self.name} IV" concede ao usuário 5% de chance de dano critico'

        elif self.level == 4:

            user.critical_chance += 5

            self.gold = 2500

            self.description = f'"{self.name} IV" concede ao usuário 5% de chance de dano critico'
            self.next_description = f'"{self.name} V" concede ao usuário 6% de chance de dano critico'

        elif self.level == 5:

            user.critical_chance += 6

            self.description = f'"{self.name} V" concede ao usuário 6% de chance de dano critico'

    def register(self, user: MainCharacter, active: bool = False) -> None:
        return super().register(user, active)

class CriticalDamage(Blessing):

    def __init__(self, name: str = '', description: str = '', next_description: str = '', gold: int = 700, level: int = 0) -> None:
        super().__init__(name, description, next_description, level, gold)
        
        self.name = 'Critical Damage'
        self.next_description = f'"{self.name}" aumenta o dano critico do usuário para 150%'

    def effect(self, user: MainCharacter) -> None:

        user.critical_damage = 0

        if self.level == 1:

            user.critical_damage += 0.25

            self.gold = 850

            self.description = f'"{self.name}" aumenta o dano critico do usuário para 125%'
            self.next_description = f'"{self.name} II" aumenta o dano critico do usuário para 150%'

        elif self.level == 2:

            user.critical_damage += 0.50

            self.gold = 1000

            self.description = f'"{self.name} II" aumenta o dano critico do usuário para 150%'
            self.next_description = f'"{self.name} III" aumenta o dano critico do usuário para 175%'

        elif self.level == 3:

            user.critical_damage += 0.75

            self.gold = 1150

            self.description = f'"{self.name} III" aumenta o dano critico do usuário para 175%'
            self.next_description = f'"{self.name} IV" aumenta o dano critico do usuário para 200%'

        elif self.level == 4:

            user.critical_damage += 1

            self.gold = 1300

            self.description = f'"{self.name} IV" aumenta o dano critico do usuário para 200%'
            self.next_description = f'"{self.name} V" aumenta o dano critico do usuário para 225%'

        elif self.level == 5:

            user.critical_damage += 1.25

            self.description = f'"{self.name} V" aumenta o dano critico do usuário para 225%'

    def register(self, user: MainCharacter, active: bool = False) -> None:
        return super().register(user, active)

class SecoundChance(Blessing):

    def __init__(self, name: str = '', description: str = '', next_description: str = '', gold: int = 2000, level: int = 0) -> None:
        super().__init__(name, description, next_description, level, gold)

        self.name = 'Secound Chance'
        self.next_description = f'"{self.name}" concede ao usuário uma segunda chance de lutar após ser derrotado, com 20% da vida total'

    def effect(self, user: MainCharacter, active: bool = False) -> None:

        if self.level == 1:

            if active:

                user.life = int(round(user.life * 0.2))

            self.gold = 3000

            self.description = f'"{self.name}" concede ao usuário uma segunda chance de lutar após ser derrotado, com 20% da vida total'
            self.next_description = f'"{self.name} II" concede ao usuário uma segunda chance de lutar após ser derrotado, com 50% da vida total'

        elif self.level == 2:

            if active:

                user.life = int(round(user.life * 0.5))
            
            self.description = f'"{self.name} II" concede ao usuário uma segunda chance de lutar após ser derrotado, com 50%', 'da vida total'

    def register(self, user: MainCharacter) -> None:
        return super().register(user)

def update_blessings(user: MainCharacter, query, active: bool = False):

    list_blessings: List[ABCMeta] = [LifeGoddessBlessing, WarGodBlessing, IronHeart, Greed, Wisdom, Dodge, CriticalChance, CriticalDamage, SecoundChance]

    for index, item in enumerate(list_blessings):

        blessing = item(level = query[index])

        if active and index == 8:
            
            blessing.effect(user, True)

        blessing.register(user)
