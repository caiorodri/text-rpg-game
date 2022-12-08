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

def xp_screen(xp_before: int, xp_after: int) -> None:

    text_decorator(' XP Ganho na Batalha ', 'cian')

    animated_text(f'\033[1;36m{xp_before}\033[m XP + \033[1;36m{xp_after - xp_before} XP\033[m -> \033[1;36m{xp_after}\033[m XP')

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
    