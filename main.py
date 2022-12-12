from time import sleep
from dungeons import dungeon1
from utils import animated_text, main_decorator, text_decorator
import re
from characters import MainCharacter
import sqlite3
import pwinput

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
        password = pwinput.pwinput(prompt='Digite sua Senha: ')

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
        password = pwinput.pwinput(prompt='Digite sua Senha: ')

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
        
    return MainCharacter(name = query[0][4], user_class = query[0][5], level = query[0][6],xp = query[0][7], dungeon = query[0][9])

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

    sleep(2)

# RANKINGS

def level_ranking(cursor: sqlite3.Cursor, name: str) -> None:

    cursor.execute('SELECT username, user_class, user_level FROM users ORDER BY user_xp DESC')
    
    result = cursor.fetchall()

    text_decorator('Ranking de Level', 'cian')

    # MÉTODO RUIM SE TIVER MUITOS USUÁRIOS

    print('TOP 10 JOGADORES\n')

    for indice, user in enumerate(result):

        if indice < 10:

            if user[0] == name:
                
                animated_text(f'\033[1;33m{indice+1}°\033[m - \033[1;33m{user[0]}\033[m / {user[1].title()} / Level {user[2]}')
                print()

            else: 
                
                if indice == 9:
                    
                    print(f'{indice+1}°- {user[0]} / {user[1].title()} / Level {user[2]}')
                    print()

                else:
                    print(f'{indice+1}° - {user[0]} / {user[1].title()} / Level {user[2]}')

        elif user[0] == name:

            animated_text(f'\033[1;33m{indice+1}°\033[m - \033[1;33m{user[0]}\033[m / {user[1].title()} / Level {user[2]}')
            print()

    animated_text(input('\033[1;33mPressione enter para voltar...\033[m'))

def deaths_ranking(cursor: sqlite3.Cursor, name: str) -> None:

    cursor.execute('SELECT username, user_class, user_level, deaths FROM users ORDER BY deaths DESC, user_dungeon ASC, user_floor ASC')
    
    result = cursor.fetchall()

    text_decorator('Ranking de Mortes', 'red')

    # MÉTODO RUIM SE TIVER MUITOS USUÁRIOS

    print('TOP 10 JOGADORES\n')

    for indice, user in enumerate(result):

        if indice < 10:

            if user[0] == name:
                
                animated_text(f'\033[1;33m{indice+1}°\033[m - \033[1;33m{user[0]}\033[m / {user[1].title()} / Level {user[2]} / Deaths: \033[1;31m{user[3]}\033[m')
                print()

            else:

                if indice == 9:

                     print(f'{indice+1}°- {user[0]} / {user[1].title()} / Level {user[2]} / Deaths: \033[1;31m{user[3]}\033[m')
                     print()

                else: print(f'{indice+1}° - {user[0]} / {user[1].title()} / Level {user[2]} / Deaths: \033[1;31m{user[3]}\033[m')

        elif user[0] == name:

            animated_text(f'\033[1;33m{indice+1}°\033[m - \033[1;33m{user[0]}\033[m / {user[1].title()} / Level {user[2]} / Deaths: \033[1;31m{user[3]}\033[m')
            print('')
    
    animated_text(input('\033[1;33mPressione enter para voltar...\033[m'))

def gold_ranking(cursor: sqlite3.Cursor, name: str) -> None:

    cursor.execute('SELECT username, user_class, user_level, user_gold FROM users ORDER BY user_gold DESC, user_level ASC')
    
    result = cursor.fetchall()

    text_decorator('Ranking de Ouro', 'yellow')

    # MÉTODO RUIM SE TIVER MUITOS USUÁRIOS

    print('TOP 10 JOGADORES\n')

    for indice, user in enumerate(result):

        if indice < 10:

            if user[0] == name:
                
                animated_text(f'\033[1;33m{indice+1}\033[m - \033[1;33m{user[0]}\033[m / {user[1].title()} / Level {user[2]} / Gold: \033[1;33m{user[3]}\033[m')
                print()

            else:
                
                if indice == 9:
                    
                    print(f'{indice+1}- {user[0]} / {user[1].title()} / Level {user[2]} / Gold: \033[1;33m{user[3]}\033[m')
                    print()

                else: print(f'{indice+1} - {user[0]} / {user[1].title()} / Level {user[2]} / Gold: \033[1;33m{user[3]}\033[m')

        elif user[0] == name:

            animated_text(f'\033[1;33m{indice+1}\033[m - \033[1;33m{user[0]}\033[m / {user[1].title()} / Level {user[2]} / Gold: \033[1;33m{user[3]}\033[m')
            print()

    animated_text(input('\033[1;33mPressione enter para voltar...\033[m'))

def dungeon_ranking(cursor: sqlite3.Cursor, name: str) -> None:

    cursor.execute('SELECT username, user_class, user_level, user_dungeon FROM users ORDER BY user_dungeon DESC, user_floor DESC, user_level ASC, user_xp ASC')
    
    result = cursor.fetchall()

    text_decorator('Ranking de Dungeon', 'cian')

    # MÉTODO RUIM SE TIVER MUITOS USUÁRIOS

    print('TOP 10 JOGADORES\n')

    for indice, user in enumerate(result):

        if indice < 10:

            if user[0] == name:
                
                animated_text(f'\033[1;33m{indice+1}°\033[m - \033[1;33m{user[0]}\033[m / {user[1].title()} / Level {user[2]} / Dungeon: {user[3]}')
                print()

            else:

                if indice == 9: 
                    
                    print(f'{indice+1}°- {user[0]} / {user[1].title()} / Level {user[2]} / Dungeon: {user[3]}')
                    print()

                else: print(f'{indice+1}° - {user[0]} / {user[1].title()} / Level {user[2]} / Dungeon: {user[3]}')

        elif user[0] == name:

            animated_text(f'\033[1;33m{indice+1}°\033[m - \033[1;33m{user[0]}\033[m / {user[1].title()} / Level {user[2]} / Duugeon: {user[3]}')
            print()

            break
    
    animated_text(input('\033[1;33mPressione enter para voltar...\033[m'))

def ranking(player: MainCharacter) -> None:

    user_choice = ''

    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()

    while user_choice != '0':

        text_decorator('Ranking', 'cian')

        animated_text('''Escolha uma Opção

[0] - Sair

[1] - Ranking de Level
[2] - Ranking de Mortes
[3] - Ranking de Gold
[4] - Ranking de Dungeon

\033[1;33mEscolha do Usuário: \033[m''', 0.025)

        user_choice = input('')

        if user_choice == '1':

            level_ranking(cursor, player.name)

        elif user_choice == '2':

            deaths_ranking(cursor, player.name)

        elif user_choice == '3':

            gold_ranking(cursor, player.name)

        elif user_choice == '4':

            dungeon_ranking(cursor, player.name)

        elif user_choice != '0':

            animated_text('\n\033[1;33mOpção Invalida\033[m')

            sleep(1)

    cursor.close()
    connection.close()
    
def menu(player: MainCharacter) -> bool:

    exit = False
    user_choice = ''

    while not exit:

        text_decorator('Menu Principal', 'cian')

        animated_text('''Escolha uma Opção

[0] - Sair

[1] - Ir para a Dungeon
[2] - Ver o Ranking
[3] - Ver Meu Status
[4] - Mudar Classe do Personagem

\033[1;33mEscolha do Usuário: \033[m''', 0.02)

        user_choice = input('')

        if user_choice == '0':

            exit = True

        elif user_choice == '1':

            exit = True

        elif user_choice == '2':

            ranking(player)
        
        elif user_choice == '3':

            player.show_stats()

            animated_text(input('\033[1;33mPresisone enter para voltar ao Menu...\033[m'))

        elif user_choice == '4':

            player.change_class()

        elif user_choice != '0':

            animated_text('\n\033[1;33mOpção Invalida!\033[m')

            sleep(1)

    if user_choice == '0':
        
        return False

    return True

def history(player: MainCharacter):

    while True:

        user_choice = menu(player)

        if not user_choice: break

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
