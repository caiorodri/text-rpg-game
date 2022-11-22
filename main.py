import getpass
from utils import main_decorator
import re
from characters import MainCharacter


def get_name() -> str:

    valid = False
    name = ''
    count = 0

    while not valid:

        valid = True
        main_decorator()
        if count == 0: name = input('Digite seu nome: ').strip()
        elif 1 <= count < 2 : name = input('Digite um nome válido: ').strip()
        else: name = input('O nome não pode conter números. ( Digite seu nome real ): ')

        num_list = '0123456789'

        for num in num_list:
            
            if num in name: valid = False

        count += 1

    return name.title()    

def get_email() -> str:

    valid = False
    email = ''
    count = 0
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,}$'

    while not valid:

        main_decorator()

        valid = True
        
        if count == 0:

            email = input('Digite seu e-mail: ').strip()

        else:

            email = input('Digite um e-mail válido (Ex: usuario@gmail.com):' )
        
        if not (re.search(regex,email)):
            
            valid = False
        
    return email

def get_password() -> str:

    valid = False
    password = ''

    main_decorator()

    while not valid:
        
        valid = True
        password = getpass.getpass(prompt='Digite sua Senha: ', stream=None)

        if len(password) < 8: 
            
            valid = False
            print('\nA senha deve conter pelo menos 8 caracteres...\n')
            continue

        if not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search("[0-9]", password) or not re.search("[_@$]", password) or re.search("\s", password): 
            
            valid = False
            print('\nA senha deve conter pelo menos 1 letra minuscula, 1 maiuscula, um número e 1 caractere especial...\n')
            continue

    return password

def get_username() -> str:
    
    valid = False
    username = ''

    main_decorator()

    while not valid:
        
        valid = True
        username = input('Digite seu nome de usuário: ').strip()
        
        if len(username) > 14:
            
            valid = False
            print('\nO nome de usuário deve conter entre 3-14 caracteres...\n')
            continue
        
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

name = get_name()
email = get_email()
password = get_password()
username = get_username()
user_class = get_class()

user = MainCharacter(username, user_class, 0, 0, 0, 0, 0)

user.show_stats(clean_screen=True)