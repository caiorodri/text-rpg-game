import getpass
from time import sleep
from dungeons import dungeon1
from utils import animated_text, main_decorator, text_decorator
import re
from characters import MainCharacter
import sqlite3

def get_name() -> str:

    valid = False
    name = ''

    while not valid:

        valid = True
        main_decorator()
        
        name = input('Digite seu nome: ').strip()

        invalid_characters = '0123456789!@#$%&*()_-<,.>;:[{}]|+-*/'

        for character in invalid_characters:
            
            if character in name:
                
                valid = False

        if not valid:

            animated_text('\n\033[1;33mNome inválido! ( Digite seu nome real )\033[m\n')
            sleep(1.5)

    return name.title()    

def get_email(name: str = 'usuario') -> str:

    valid = False
    email = ''
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,}$'

    while not valid:

        valid = True
        main_decorator()

        email = input('Digite seu e-mail: ').strip()

        if not (re.search(regex,email)):
            
            valid = False

            animated_text(f'\n\033[1;33mDigite um e-mail válido (Ex: {name.lower()}@gmail.com)\033[m\n' )
            sleep(1.5)        
        
    return email

def get_password() -> str:

    valid = False
    password = ''

    while not valid:

        main_decorator()

        valid = True
        password = getpass.getpass(prompt='Digite sua Senha: ', stream=None)

        if len(password) < 8: 
            
            valid = False
            animated_text('\n\033[1;33mA senha deve conter pelo menos 8 caracteres...\033[m\n')
            sleep(1)
            continue

        if not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search("[0-9]", password) or not re.search("[_@$]", password) or re.search("\s", password): 
            
            valid = False
            animated_text('\n\033[1;33mA senha deve conter pelo menos 1 letra minuscula, 1 maiuscula, um número e 1 caractere especial...\033[m\n')
            sleep(1)
            continue

    return password

def get_username(query) -> str:
    
    valid = False
    username = ''

    while not valid:

        main_decorator()

        valid = True
        username = input('Digite seu nome de usuário: ').strip()
        
        if len(username) > 14 or len(username) < 3:
            
            valid = False
            print('\nO nome de usuário deve conter entre 3-14 caracteres...\n')
            continue
        
        try:
            
            for users in query:

                if username == users[4]:

                    animated_text('\n\033[1;33mNome de Usuário já esta sendo usado!\033[m\n')
                    valid = False
                    sleep(2)
                    continue
        
        except IndexError:

            pass

    return username

def get_class() -> str:

    valid = False
    user_class = ''

    main_decorator()

    print('''Escolha uma classe para iniciar

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

        else: print('\nEscolha inválida!\n')
    
    return user_class

def check_email(name, query) -> str:

    valid = False
    email = ''

    while not valid:

        valid = True

        email = get_email(name)

        regex = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

        if not (re.search(regex, email)): valid = False

        if not valid:

            animated_text('\n\033[1;33mEmail inválido!\033[m\n')
            valid = False
            sleep(2)
            continue
        
        try:
            
            for users in query:

                if email == users[2]:

                    animated_text('\n\033[1;33mEmail existente! Tente fazer login.\033[m\n')
                    valid = False
                    sleep(2)
                    continue

        except IndexError:

            pass

    return email

def register() -> MainCharacter:

    valid = False

    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users')

    query = cursor.fetchall()

    name = ''
    password = ''
    email = ''
    username = ''
    user_class = ''

    while not valid:
        
        valid = True

        name = get_name()
        email = check_email(name, query)        
        password = get_password()

        if len(password) < 8:

            valid = False
            animated_text('\n\033[1;33mA senha deve conter 8 ou mais caracteres!\033[m\n')
            continue

        username = get_username(query)
        
        user_class = get_class()

    user = MainCharacter(username, user_class)

    cursor.execute(f"INSERT INTO users ('name', 'email', 'password', 'username', 'user_class') VALUES ('{name}', '{email}', '{password}', '{username}','{user_class}')")

    connection.commit()
    cursor.close()
    connection.close()

    return user

def login() -> MainCharacter:

    valid = False
    query = []

    while not valid:

        valid = True

        email = get_email()
        password = getpass.getpass(prompt='Digite sua Senha: ', stream=None)

        connection = sqlite3.connect('user.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
        query = cursor.fetchall()

        try:
            
            right_password = query[0][3]

        except IndexError:

            animated_text('\n\033[1;33Email ou senha invalidos!\033[m\n')
            valid = False
            sleep(2)

            continue

        if right_password != password:

            valid = False
            animated_text('\n\033[1;33Email ou senha invalidos!\033[m\n')
            continue

        cursor.close()
        connection.close()
        
    return MainCharacter(name = query[0][1], user_class = query[0][5], level = query[0][6],xp = query[0][7], dungeon = query[0][8])

def init():

    valid = False

    player = MainCharacter('', '')
    user_choice = ''

    while not valid:

        valid = True

        text_decorator('My Little Game', 'cian')

        animated_text('''Escolha uma opção

[0] - Sair

[1] - Login
[2] - Registrar-me

\033[1;33mEscolha do Usuário:\033[m ''')
    
        user_choice = input('')

        if user_choice == '0': break

        if user_choice == '1': player = login()

        elif user_choice == '2': player = register()

        else:

            valid = False
            print()
            animated_text('\033[1;31mOpção invalida! Digite "0", "1" ou "2".\033[m')
            sleep(2)
            continue
    
    if user_choice != '0':
        
        player.show_stats()

        animated_text('\033[1;33mPressione enter para continuar...\033[m')

        input(' ')

        history(player)

    animated_text('\n\033[1;32mObrigado por jogar meu jogo! Volte sempre\033[m\n')

    input('\n\033[1;33mPressione enter para continuar...\033[m')

def history(player: MainCharacter):

    while True:

        if player.dungeon == 1:
    
            result_dungeon = dungeon1(player)

            player.check_stats()

            if result_dungeon:

                player.dungeon += 1

        player.level_up()
        player.update_stats()

        if player.dungeon == 2:

            break

init()