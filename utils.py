import os

def text_decorator(text: str, decorator: str) -> None:

    print(decorator * (len(text) + 2))
    print(f' {text}')
    print(decorator * (len(text) + 2))


def main_decorator():

    clean()
    print('=' * (len("My First Text RPG") + 2))
    print(f" \033[1;36mMy First Text RPG\033[m")
    print('=' * (len("My First Text RPG") + 2))
    print()

def clean():

    os.system('cls' if os.name == 'nt' else 'clear')


def coloring_text(text, color):

    if color == 'white':

        return(f'\033[1;38m{text}\033[m')

    if color == 'red':

        return(f'\033[1;31m{text}\033[m')

    if color == 'green':

        return(f'\033[1;32m{text}\033[m')

    if color == 'yellow':

        return(f'\033[1;33m{text}\033[m')

    if color == 'purple':

        return(f'\033[1;34m{text}\033[m')

    if color == 'cian':

        return(f'\033[1;36m{text}\033[m')


