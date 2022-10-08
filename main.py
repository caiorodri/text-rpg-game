from utils import main_decorator
import re


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

        valid = True
        
        if count == 0:

            email = input('Digite seu e-mail: ').strip()

        else:

            email = input('Digite um e-mail válido (Ex: usuario@gmail.com):' )
        
        if not (re.search(regex,email)):
            
            valid = False
        
    return email