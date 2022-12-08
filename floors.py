from time import sleep
from typing import List
from characters import Monster, MainCharacter
from random import choice, randint
from utils import animated_text, clean, lose_floors, text_decorator, resource_screen


def fight_screen(player: MainCharacter, monsters: List[Monster], floor: str) -> None:

    floor_decorator(floor)

    print(f'\033[1;36m{player.name}\033[m {player.user_class.capitalize()} lvl {player.level} - (\033[1;32m{player.life}\033[m HP) (\033[1;36m{player.damage}\033[m ATK) (\033[1;33m{player.shield}\033[m DEF)')

    print()

    for index, monster in enumerate(monsters):

        print(f'[{index+1}] \033[1;31m{monster.name.capitalize()}\033[m lvl {monster.level} - (\033[1;31m{monster.life}\033[m HP) (\033[1;31m{monster.damage}\033[m ATK) (\033[1;33m{monster.shield}\033[m DEF)')

def damage_screen(player: MainCharacter, monsters: List[Monster], player_target: int, floor: str):

    floor_decorator(floor)

    monsters_damage = 0

    print(f'\033[1;36m{player.name}\033[m {player.user_class.capitalize()} lvl {player.level} - (\033[1;32m{player.life}\033[m HP) (\033[1;36m{player.damage}\033[m ATK) (\033[1;33m{player.shield}\033[m DEF)')

    print()

    for index, monster in enumerate(monsters):

        if monster.life > 0: 

            if index == player_target:

                # ATAQUE DO USUÁRIO

                print(f'[{index+1}] \033[1;31m{monster.name.capitalize()}\033[m lvl {monster.level} - (\033[1;31m{monster.life}\033[m HP) (\033[1;31m{monster.damage}\033[m ATK) (\033[1;33m{monster.shield}\033[m DEF)', end=' ')

                if player.damage - monster.shield <= 0:                 
                    
                    animated_text(f'[\033[1;31m{monster.life}\033[m HP - \033[1;36m0\033[m ->', 0.035)
                    
                else:

                    animated_text(f'[\033[1;31m{monster.life}\033[m HP - \033[1;36m{player.damage - monster.shield}\033[m ->', 0.035)

                if (monster.life - (player.damage - monster.shield)) <= 0:

                    animated_text(' \033[1;31m0\033[m HP] ( \033[1;31mDIED\033[m )\n', 0.035)

                else:

                    animated_text(f' \033[1;31m{monster.life - (player.damage - monster.shield)}\033[m HP]\n', 0.035)

                if (player.damage - monster.shield) > 0:
    
                    monster.life -= (player.damage - monster.shield)
                
            else:

                print(f'[{index+1}] \033[1;31m{monster.name.capitalize()}\033[m lvl {monster.level} - (\033[1;31m{monster.life}\033[m HP) (\033[1;31m{monster.damage}\033[m ATK) (\033[1;33m{monster.shield}\033[m DEF)')

            if monster.life > 0:

                monsters_damage += monster.damage

    animated_text(input('\n\033[1;33mPressione enter para continuar...\033[m'))

    floor_decorator(floor)

    # ATAQUE DOS MONSTROS

    print(f'\033[1;36m{player.name}\033[m {player.user_class.capitalize()} lvl {player.level} - (\033[1;32m{player.life}\033[m HP) (\033[1;36m{player.damage}\033[m ATK) (\033[1;33m{player.shield}\033[m DEF)', end=' ')

    if monsters_damage - player.shield <= 0:
            
        animated_text(f'[\033[1;32m{player.life}\033[m HP - \033[1;31m0\033[m -> \033[1;32m{player.life}\033[m HP]')

    else:

        if player.life - (monsters_damage - player.shield) <= 0:

            animated_text(f'[\033[1;32m{player.life}\033[m HP - \033[1;31m{monsters_damage - player.shield}\033[m -> \033[1;32m0\033[m HP]')

        else:
            
            animated_text(f'[\033[1;32m{player.life}\033[m HP - \033[1;31m{monsters_damage - player.shield}\033[m -> \033[1;32m{player.life - (monsters_damage - player.shield)}\033[m HP]')

        player.life -= (monsters_damage - player.shield)

    print()

    animated_text(input('\n\033[1;33mPressione enter para continuar...\033[m'))

def fight(player: MainCharacter, monsters: List[Monster], floor: str) -> bool:

    player.check_level()
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

                if user_target >= 0 and user_target < len(monsters):
                    
                    valid = True

            except: pass
            
            if not valid:

                animated_text('\033[1;33m\nEscolha um alvo válido!\033[m')

                sleep(1.5)
        
        # ATAQUES

        damage_screen(player, monsters, user_target, floor)

        # CHECAGEM DOS MONSTROS VIVOS

        for index, monster in enumerate(monsters):

            if monster.life <= 0:
                    
                player.xp += monster.xp
                player.gold += monster.gold

                monsters.pop(index)

        if len(monsters) == 0:

            battle_result = True

        if player.life <= 0:

            battle_result = False
            player.deaths += 1

            player.update_deaths()

            lose_floors(player.floor)

            if player.floor <= 3: player.floor = 1
            
            else: player.floor -= 3

    return battle_result

def get_monsters(monsters: List[str], min_level: int = 1, max_level: int = 3, min_quantity_monster: int = 1, max_quantity_monster: int = 3, boss: List[str] = ['nothing']) -> list:

    list_monsters = []

    if boss[0] != 'nothing':

        list_monsters.append(Monster(choice(boss), 3))

    quantity_monsters = randint(min_quantity_monster, max_quantity_monster)

    for indice in range(1, quantity_monsters+1):

        level_monster = randint(min_level, max_level)

        list_monsters.append(Monster(choice(monsters), level_monster))

    for monster in list_monsters:

        monster.check_stats()

    return list_monsters

def floor_decorator(floor):

    clean()

    text_decorator(f'         {floor}         ', color='yellow')

def floor1(player: MainCharacter, monster: List[str], level_min_monster: int = 1, level_max_monster: int = 3 , min_quantity_monsters: int = 1, max_quantity_monsters: int = 3) -> bool:

    battle_result = True

    for indice in range(2):

        if battle_result:

            xp_before_battle = player.xp
            gold_before_battle = player.gold

            monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

            floor_decorator('Andar 1')

            battle_result = fight(player, monsters, 'Andar 1')

            xp_after_battle = player.xp
            gold_after_battle = player.gold

            resource_screen(xp_before_battle, xp_after_battle, gold_before_battle, gold_after_battle)
            player.level_up()
 
    if battle_result: player.floor += 1

    return battle_result

def floor2(player: MainCharacter, monster: List[str], level_min_monster: int = 1, level_max_monster: int = 3 , min_quantity_monsters: int = 2, max_quantity_monsters: int = 3) -> bool:

    battle_result = True

    for indice in range(2):

        if battle_result:

            xp_before_battle = player.xp
            gold_before_battle = player.gold

            monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

            floor_decorator('Andar 2')
            
            battle_result = fight(player, monsters, 'Andar 2')

            xp_after_battle = player.xp
            gold_after_battle = player.gold

            resource_screen(xp_before_battle, xp_after_battle, gold_before_battle, gold_after_battle)
            player.level_up()
 
    if battle_result: player.floor += 1

    return battle_result

def floor3(player: MainCharacter, monster: List[str], level_min_monster: int = 2, level_max_monster: int = 4 , min_quantity_monsters: int = 2, max_quantity_monsters: int = 3) -> bool:

    battle_result = True

    for indice in range(2):

        if battle_result:

            xp_before_battle = player.xp
            gold_before_battle = player.gold

            monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

            floor_decorator('Andar 3')

            battle_result = fight(player, monsters, 'Andar 3')

            xp_after_battle = player.xp
            gold_after_battle = player.gold
            
            resource_screen(xp_before_battle, xp_after_battle, gold_before_battle, gold_after_battle)
            player.level_up()
  
    if battle_result: player.floor += 1

    return battle_result

def floor4(player: MainCharacter, monster: List[str], level_min_monster: int = 3, level_max_monster: int = 5 , min_quantity_monsters: int = 2, max_quantity_monsters: int = 3) -> bool:

    battle_result = True

    for indice in range(2):

        if battle_result:

            xp_before_battle = player.xp
            gold_before_battle = player.gold

            monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

            floor_decorator('Andar 4')

            battle_result = fight(player, monsters, 'Andar 4')

            xp_after_battle = player.xp
            gold_after_battle = player.gold
            
            resource_screen(xp_before_battle, xp_after_battle, gold_before_battle, gold_after_battle)
            player.level_up()
    
    if battle_result: player.floor += 1

    return battle_result

def floor5(player: MainCharacter, monster: List[str], level_min_monster: int = 4, level_max_monster: int = 6 , min_quantity_monsters: int = 3, max_quantity_monsters: int = 5) -> bool:

    battle_result = True

    for indice in range(2):

        if battle_result:

            xp_before_battle = player.xp
            gold_before_battle = player.gold

            monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

            floor_decorator('Andar 5')

            battle_result = fight(player, monsters, 'Andar 5')

            xp_after_battle = player.xp
            gold_after_battle = player.gold
            
            resource_screen(xp_before_battle, xp_after_battle, gold_before_battle, gold_after_battle)
            player.level_up()
  
    if battle_result: player.floor += 1

    return battle_result

def floor6(player: MainCharacter, monster: List[str], level_min_monster: int = 5, level_max_monster: int = 7 , min_quantity_monsters: int = 2, max_quantity_monsters: int = 3) -> bool:

    battle_result = True

    for indice in range(2):

        if battle_result:

            xp_before_battle = player.xp
            gold_before_battle = player.gold

            monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

            floor_decorator('Andar 6')

            battle_result = fight(player, monsters, 'Andar 6')

            xp_after_battle = player.xp
            gold_after_battle = player.gold
            
            resource_screen(xp_before_battle, xp_after_battle, gold_before_battle, gold_after_battle)
            player.level_up()
  
    if battle_result: player.floor += 1

    return battle_result

def floor7(player: MainCharacter, monster: List[str], level_min_monster: int = 6, level_max_monster: int = 8 , min_quantity_monsters: int = 2, max_quantity_monsters: int = 3) -> bool:

    battle_result = True

    for indice in range(2):

        if battle_result:

            xp_before_battle = player.xp
            gold_before_battle = player.gold

            monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

            floor_decorator('Andar 7')

            battle_result = fight(player, monsters, 'Andar 7')

            xp_after_battle = player.xp
            gold_after_battle = player.gold
            
            resource_screen(xp_before_battle, xp_after_battle, gold_before_battle, gold_after_battle)
            player.level_up()
  
    if battle_result: player.floor += 1

    return battle_result

def floor8(player: MainCharacter, monster: List[str], level_min_monster: int = 7, level_max_monster: int = 9 , min_quantity_monsters: int = 2, max_quantity_monsters: int = 3) -> bool:

    battle_result = True

    for indice in range(2):

        if battle_result:

            xp_before_battle = player.xp
            gold_before_battle = player.gold

            monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

            floor_decorator('Andar 8')

            battle_result = fight(player, monsters, 'Andar 8')

            xp_after_battle = player.xp
            gold_after_battle = player.gold
            
            resource_screen(xp_before_battle, xp_after_battle, gold_before_battle, gold_after_battle)
            player.level_up()
  
    if battle_result: player.floor += 1

    return battle_result

def floor9(player: MainCharacter, monster: List[str], level_min_monster: int = 8, level_max_monster: int = 10 , min_quantity_monsters: int = 2, max_quantity_monsters: int = 3) -> bool:

    battle_result = True

    for indice in range(2):

        if battle_result:

            xp_before_battle = player.xp
            gold_before_battle = player.gold

            monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters)

            floor_decorator('Andar 9')

            battle_result = fight(player, monsters, 'Andar 9')

            xp_after_battle = player.xp
            gold_after_battle = player.gold
            
            resource_screen(xp_before_battle, xp_after_battle, gold_before_battle, gold_after_battle)
            player.level_up()
  
    if battle_result: player.floor += 1

    return battle_result

def floor10(player: MainCharacter, monster: List[str], boss: List[str], level_min_monster: int = 1, level_max_monster: int = 10 , min_quantity_monsters: int = 1, max_quantity_monsters: int = 3) -> bool:

    xp_before_battle = player.xp
    gold_before_battle = player.gold

    monsters = get_monsters(monster, level_min_monster, level_max_monster, min_quantity_monsters, max_quantity_monsters, boss)

    floor_decorator('Andar 10')

    battle_result = fight(player, monsters, 'Andar 10')

    xp_after_battle = player.xp
    gold_after_battle = player.gold
    
    resource_screen(xp_before_battle, xp_after_battle, gold_before_battle, gold_after_battle)

    return battle_result
