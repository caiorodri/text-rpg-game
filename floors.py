from time import sleep
from typing import List
from characters import Monster, MainCharacter
from random import randint
from utils import animated_text, clean, text_decorator


def fight_screen(player: MainCharacter, monsters: List[Monster], floor: str) -> None:

    floor_decorator(floor)

    print(f'\033[1;36m{player.name}\033[m {player.user_class.capitalize()} lvl {player.level} - (\033[1;32m{player.life}\033[m HP) (\033[1;36m{player.damage}\033[m ATK)')

    print()

    for index, monster in enumerate(monsters):

        monster.check_stats()

        print(f'[{index+1}] \033[1;31m{monster.name.capitalize()}\033[m lvl {monster.level} - (\033[1;31m{monster.life}\033[m HP) (\033[1;31m{monster.damage}\033[m ATK)')

def damage_screen(player: MainCharacter, monsters: List[Monster], player_target: int, floor: str) -> list:

    floor_decorator(floor)

    monsters_damage = 0

    print(f'\033[1;36m{player.name}\033[m {player.user_class.capitalize()} lvl {player.level} - (\033[1;32m{player.life}\033[m HP) (\033[1;36m{player.damage}\033[m ATK)')

    for index, monster in enumerate(monsters):

        if monster.life > 0:

            if index == player_target:

                # ATAQUE DO USUÁRIO

                print(f'[{index+1}] \033[1;31m{monster.name.capitalize()}\033[m lvl {monster.level} - (\033[1;31m{monster.life}\033[m HP) (\033[1;31m{monster.damage}\033[m ATK) - [\033[1;31m{monster.life}\033[m HP - \033[1;36m{player.damage}\033[m ->', end='')
                
                if (monster.life - player.damage) <= 0:

                    print(' \033[1;31m0\033[m HP] ( \033[1;31mDIED\033[m ) ')

                else:

                    print(f' \033[1;31m{monster.life - player.damage}\033[m HP]')

                monster.life -= player.damage

            else:

                print(f'[{index+1}] \033[1;31m{monster.name.capitalize()}\033[m lvl {monster.level} - (\033[1;31m{monster.life}\033[m HP) (\033[1;31m{monster.damage}\033[m ATK)')

            if monster.life > 0:

                monsters_damage += monster.damage

    print()

    animated_text(input('\nPressione enter para continuar...'))

    floor_decorator(floor)

    # ATAQUE DOS MONSTROS

    print(f'\033[1;36m{player.name}\033[m {player.user_class.capitalize()} lvl {player.level} - (\033[1;32m{player.life}\033[m HP) (\033[1;36m{player.damage}\033[m ATK)', end=' ')

    animated_text(f'[\033[1;32m{player.life}\033[m HP - \033[1;31m{monsters_damage}\033[m -> \033[1;32m{player.life - monsters_damage}\033[m HP]')

    player.life -= monsters_damage

    print()

    animated_text(input('\nPressione enter para continuar...'))

    return [player.life, monsters]

def fight(player: MainCharacter, monsters: List[Monster], floor: str) -> str:

    player.check_stats()

    battle_result = 'Andamento'

    user_target = 0

    while battle_result == 'Andamento':

        valid = False

        while not valid:

            fight_screen(player, monsters, floor)

            print()

            try:
                
                user_target = int(input('Escolha um inimigo para atacar: ').strip())-1

                if user_target >= 0 and user_target <= len(monsters):
                    
                    valid = True

            except: pass
            
            if not valid:

                animated_text('\033[1;33m\nEscolha um alvo válido!\033[m')

                sleep(1.5)
        
        # ATAQUES

        player.life, monsters = damage_screen(player, monsters, user_target, floor)

        # CHECAGEM DOS MONSTROS VIVOS

        for index, monster in enumerate(monsters):

            if monster.life <= 0:
                    
                monsters.pop(index)

        if len(monsters) == 0:

            battle_result = 'win'

        if player.life <= 0:

            battle_result = 'lose'


    return battle_result

def get_monsters(name: str, min_level: int = 1, max_level: int = 3, min_quantity_monster: int = 1, max_quantity_monster: int = 3, boss: str = 'nothing') -> list:

    monsters = []

    if boss == 'nothing':

        quantity_monsters = randint(min_quantity_monster, max_quantity_monster)

        for indice in range(1, quantity_monsters+1):

            level_monster = randint(min_level, max_level)

            monsters.append(Monster(name, level_monster))

        for monster in monsters:

            monster.check_stats()

        return monsters

    else:

        monsters.append

def floor_decorator(floor):

    clean()

    text_decorator(f'         {floor}         ', color='yellow')

# DUNGEON 1

def floor1(player: MainCharacter, monster: str, level_min_monster: int = 1, level_max_monster: int = 3 , min_quantity_monsters: int = 1, max_quantity_monsters: int = 3):

    monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

    floor_decorator('Andar 1')

    battle_result = fight(player, monsters, 'Andar 1')

    return battle_result

def floor2(player: MainCharacter, monster: str, level_min_monster: int = 1, level_max_monster: int = 3 , min_quantity_monsters: int = 1, max_quantity_monsters: int = 3):

    monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

    floor_decorator('Andar 2')

    battle_result = fight(player, monsters, 'Andar 2')

    return battle_result

def floor3(player: MainCharacter, monster: str, level_min_monster: int = 1, level_max_monster: int = 3 , min_quantity_monsters: int = 1, max_quantity_monsters: int = 3):

    monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

    floor_decorator('Andar 3')

    battle_result = fight(player, monsters, 'Andar 3')

    return battle_result

def floor4(player: MainCharacter, monster: str, level_min_monster: int = 1, level_max_monster: int = 3 , min_quantity_monsters: int = 1, max_quantity_monsters: int = 3):

    monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

    floor_decorator('Andar 4')

    battle_result = fight(player, monsters, 'Andar 4')

    return battle_result

def floor5(player: MainCharacter, monster: str, level_min_monster: int = 1, level_max_monster: int = 3 , min_quantity_monsters: int = 1, max_quantity_monsters: int = 3):

    monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

    floor_decorator('Andar 5')

    battle_result = fight(player, monsters, 'Andar 5')

    return battle_result

def floor6(player: MainCharacter, monster: str, level_min_monster: int = 1, level_max_monster: int = 3 , min_quantity_monsters: int = 1, max_quantity_monsters: int = 3):

    monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

    floor_decorator('Andar 6')

    battle_result = fight(player, monsters, 'Andar 6')

    return battle_result

def floor7(player: MainCharacter, monster: str, level_min_monster: int = 1, level_max_monster: int = 3 , min_quantity_monsters: int = 1, max_quantity_monsters: int = 3):

    monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

    floor_decorator('Andar 7')

    battle_result = fight(player, monsters, 'Andar 7')

    return battle_result

def floor8(player: MainCharacter, monster: str, level_min_monster: int = 1, level_max_monster: int = 3 , min_quantity_monsters: int = 1, max_quantity_monsters: int = 3):

    monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

    floor_decorator('Andar 8')

    battle_result = fight(player, monsters, 'Andar 8')

    return battle_result

def floor9(player: MainCharacter, monster: str, level_min_monster: int = 1, level_max_monster: int = 3 , min_quantity_monsters: int = 1, max_quantity_monsters: int = 3):

    monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

    floor_decorator('Andar 9')

    battle_result = fight(player, monsters, 'Andar 9')

    return battle_result

def floor10(player: MainCharacter, monster: str, boss: str, level_min_monster: int = 1, level_max_monster: int = 3 , min_quantity_monsters: int = 1, max_quantity_monsters: int = 3):

    monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

    boss = get_monsters('slime', )

    floor_decorator('Andar 10')

    battle_result = fight(player, monsters, 'Andar 10')

    return battle_result


    
