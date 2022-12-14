import json
import os
from time import sleep

def text_decorator(text: str, color: str = 'white', decorator: str = '=') -> None:

    clean()

    if color == 'white':
        print(decorator * (len(text) + 2))
        print('', coloring_text(text, 'white'))
        print(decorator * (len(text) + 2))
    
    elif color == 'red':
        print(decorator * (len(text) + 2))
        print('', coloring_text(text, 'red'))
        print(decorator * (len(text) + 2))
    
    elif color == 'green':
        print(decorator * (len(text) + 2))
        print('', coloring_text(text, 'green'))
        print(decorator * (len(text) + 2))
    
    elif color == 'yellow':
        print(decorator * (len(text) + 2))
        print('', coloring_text(text, 'yellow'))
        print(decorator * (len(text) + 2))

    elif color == 'purple':
        print(decorator * (len(text) + 2))
        print('', coloring_text(text, 'purple'))
        print(decorator * (len(text) + 2))

    elif color == 'pink':
        print(decorator * (len(text) + 2))
        print('', coloring_text(text, 'pink'))
        print(decorator * (len(text) + 2))

    elif color == 'cian':
        print(decorator * (len(text) + 2))
        print('', coloring_text(text, 'cian'))
        print(decorator * (len(text) + 2))
    
    print()

def main_decorator():

    clean()
    print('=' * (len("My First Text RPG") + 2))
    print(f" \033[1;36mMy First Text RPG\033[m")
    print('=' * (len("My First Text RPG") + 2))
    print()

def clean():

    os.system('cls' if os.name == 'nt' else 'clear')

def coloring_text(text: str, color: str) -> str:

    if color == 'red':

        return(f'\033[1;31m{text}\033[m')

    if color == 'green':

        return(f'\033[1;32m{text}\033[m')

    if color == 'yellow':

        return(f'\033[1;33m{text}\033[m')

    if color == 'purple':

        return(f'\033[1;34m{text}\033[m')

    if color == 'pink':

        return(f'\033[1;35m{text}\033[m')

    if color == 'cian':

        return(f'\033[1;36m{text}\033[m')

    else:

        return(f'\033[1;38m{text}\033[m')

def animated_text(text: str, time: float = 0.05):

    for letter in text:

        print(letter, end='')
        sleep(time)

def resource_screen(xp_before: int, xp_after: int, gold_before: int, gold_after: int) -> None:

    text_decorator(' Ganhos da Batalha ', 'cian')

    animated_text(f'\033[1;36m{xp_before}\033[m XP + \033[1;36m{xp_after - xp_before}\033[m XP -> \033[1;36m{xp_after}\033[m XP\n')

    animated_text(f'\033[1;33m{gold_before}\033[m G + \033[1;33m{gold_after - gold_before}\033[m G -> \033[1;33m{gold_after}\033[m G')

    animated_text(input("\n\n\033[1;33mPressione enter para continuar...\033[m"))

def lose_floors(floor):

    text_decorator('Derrota na Batalha', 'red')

    if floor <= 3:
        
        animated_text(f'''floor {floor}

| | | |        
| | | |
| | | |

floor 1
''')

    else:

        animated_text(f'''floor {floor}

| | | | |
| | | | |
| | | | |

floor {floor - 3}
''')         

    print()
    
    animated_text(input('\033[1;33mPresisone enter para continuar...\033[m'))

def write_stats():

    dict_stats = {"leveis" : {}, "xp" : {}}

    heroes_list = ["guerreiro", "mago", "arqueiro"]

    xp = 100
    xp_increase = 100

    warrior_atk = 25
    warrior_atk_increase = 3
    warrior_life = 100
    warrior_life_increase = 10
    warrior_shield = 10
    warrior_shield_increase = 2

    mage_atk = 30
    mage_atk_increase = 6
    mage_life = 75
    mage_life_increase = 8
    mage_shield = 7
    mage_shield_increase = 1

    archer_atk = 25
    archer_atk_increase = 5
    archer_life = 85
    archer_life_increase = 9
    archer_shield = 6
    archer_shield_increase = 1

    for indice in range(1, 51):

        dict_stats["leveis"][f"level{indice}"] = {f"{heroes_list[0]}" : {"vida" : warrior_life, "ataque" : warrior_atk,"escudo" : warrior_shield}, f"{heroes_list[1]}" : {"vida" : mage_life, "ataque" : mage_atk, "escudo" : mage_shield}, f"{heroes_list[2]}" : {"vida" : archer_life, "ataque" : archer_atk, "escudo" : archer_shield}}

        warrior_atk += warrior_atk_increase
        warrior_life += warrior_life_increase
        warrior_shield += warrior_shield_increase        

        mage_atk += mage_atk_increase
        mage_life += mage_life_increase
        mage_shield += mage_shield_increase

        archer_atk += archer_atk_increase
        archer_life += archer_life_increase
        archer_shield += archer_shield_increase

    for indice in range(1, 51):
        
        dict_stats["xp"][f"level{indice}"] = xp

        xp += xp_increase

        if indice % 3 == 0:

            xp_increase += 150
    
    with open('stats.json', 'w') as file:
        json.dump(dict_stats, file, indent=4)
