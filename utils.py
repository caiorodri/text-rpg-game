import os

def text_decorator(text: str, decorator: str) -> None:

    print(decorator * (len(text) + 2))
    print(f' {text}')
    print(decorator * (len(text) + 2))


def main_decorator():

    clean()
    print('=' * (len("My First Text RPG") + 2))
    print(f" My First Text RPG")
    print('=' * (len("My First Text RPG") + 2))
    print()

def clean():

    os.system('cls' if os.name == 'nt' else 'clear')
