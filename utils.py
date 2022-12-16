from email.message import EmailMessage
import json
import os
from random import randint
import smtplib
from time import sleep
import mysql.connector

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
    print('=' * (len("Dungeon of Adventure") + 2))
    print(f" \033[1;36mDungeon of Adventure\033[m")
    print('=' * (len("Dungeon of Adventure") + 2))
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

    animated_text(f'\033[1;36m{xp_before}\033[m XP + \033[1;36m{xp_after - xp_before}\033[m XP -> \033[1;36m{xp_after}\033[m XP\n', 0.015)

    animated_text(f'\033[1;33m{gold_before}\033[m G + \033[1;33m{gold_after - gold_before}\033[m G -> \033[1;33m{gold_after}\033[m G', 0.015)

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

| | | | 
| | | | 
| | | | 

floor {floor - 3}
''')         

    print()
    
    animated_text(input('\033[1;33mPresisone enter para continuar...\033[m'))

def write_stats():

    dict_stats = {"leveis" : {}, "xp" : {"level1" : 0,}}

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

    for indice in range(2, 51):
        
        dict_stats["xp"][f"level{indice}"] = xp

        xp += xp_increase

        if indice % 3 == 0:

            xp_increase += 150
    
    with open('stats.json', 'w') as file:
        json.dump(dict_stats, file, indent=4)

def write_monster_stats():

    dict_stats = {"monstros" : {}}

    monster_list = ["slime", "goblin", "esqueleto", "orc"]

    slime_atk = 15
    slime_atk_increase = 5
    slime_life = 20
    slime_life_increase = 9
    slime_shield = 1
    slime_shield_increase = 1
    slime_xp = 10
    slime_xp_increase = 5
    slime_gold = 15
    slime_gold_increase = 5

    goblin_atk = 50
    goblin_atk_increase = 7
    goblin_life = 90
    goblin_life_increase = 7
    goblin_shield = 10
    goblin_shield_increase = 1
    goblin_xp = 50
    goblin_xp_increase = 7
    goblin_gold = 55
    goblin_gold_increase = 10

    esqueleto_atk = 100
    esqueleto_atk_increase = 9
    esqueleto_life = 140
    esqueleto_life_increase = 4
    esqueleto_shield = 20
    esqueleto_shield_increase = 2
    esqueleto_xp = 110
    esqueleto_xp_increase = 8
    esqueleto_gold = 110
    esqueleto_gold_increase = 8

    orc_atk = 180
    orc_atk_increase = 5
    orc_life = 200
    orc_life_increase = 7
    orc_shield = 40
    orc_shield_increase = 3
    orc_xp = 180
    orc_xp_increase = 10
    orc_gold = 200
    orc_gold_increase = 15

    for indice in range(1, 21):

        dict_stats["monstros"][f"level{indice}"] = {f"{monster_list[0]}" : {"vida" : slime_life, "ataque" : slime_atk,"escudo" : slime_shield, "xp" : slime_xp, "gold" : slime_gold}, f"{monster_list[1]}" : {"vida" : goblin_life, "ataque" : goblin_atk, "escudo" : goblin_shield, "xp" : goblin_xp, "gold" : goblin_gold}, f"{monster_list[2]}" : {"vida" : esqueleto_life, "ataque" : esqueleto_atk, "escudo" : esqueleto_shield, "xp" : esqueleto_xp, "gold" : esqueleto_gold}, f"{monster_list[3]}" : {"vida" : orc_life, "ataque" : orc_atk, "escudo" : orc_shield, "xp" : orc_xp, "gold" : orc_gold}}

        slime_atk += slime_atk_increase
        slime_life += slime_life_increase
        slime_shield += slime_shield_increase
        slime_xp += slime_xp_increase
        slime_gold += slime_gold_increase

        goblin_atk += goblin_atk_increase
        goblin_life += goblin_life_increase
        goblin_shield += goblin_shield_increase
        goblin_xp += goblin_xp_increase
        goblin_gold += goblin_gold_increase

        esqueleto_atk += esqueleto_atk_increase
        esqueleto_life += esqueleto_life_increase
        esqueleto_shield += esqueleto_shield_increase
        esqueleto_xp += esqueleto_xp_increase
        esqueleto_gold += esqueleto_gold_increase

        orc_atk += orc_atk_increase
        orc_life += orc_life_increase
        orc_shield += orc_shield_increase
        orc_xp += orc_xp_increase
        orc_gold += orc_gold_increase

    with open('monsters.json', 'w') as file:
        json.dump(dict_stats, file, indent=4)

def check_email_valid(email: str) -> str:

    connection = mysql.connector.connect(host='localhost', database='dbtextrpg', user='root', password='')
    cursor = connection.cursor()

    number = randint(100000, 999999)

    cursor.execute('SELECT email, password FROM users WHERE id = 2')

    result = cursor.fetchall()

    email_from = result[0][0]
    password = result[0][1]

    message = EmailMessage()
    message['subject'] = 'Verificação de Email'
    message['From'] = email_from
    message['To'] = email
    message.set_content(f'Código: {number}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(email_from, password)
        smtp.send_message(message)

    return str(number)