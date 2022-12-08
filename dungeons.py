from characters import MainCharacter
from floors import *
from utils import animated_text, clean, text_decorator


def dungeon_decorator(dungeon):

    clean()

    text_decorator(f'         {dungeon}         ', color='cian')

def win_message(dungeon, floor):

        dungeon_decorator(dungeon)

        animated_text(f'Parabéns! você limpou com sucesso o {floor}° andar da {dungeon}')

        animated_text(input('\n\n\033[1;33mPressione enter para prosseguir para o proxímo andar...\033[m'))

def dungeon(dungeon: str, player: MainCharacter, monster: List[str]) -> bool:
    
    win = False
    result_floor = False

    while not win: 
    
        if player.floor == 1:
        
            result_floor = floor1(player, monster)

            player.level_up()
            
            player.update_stats()

            if result_floor:

                win_message(dungeon, '1')

        if player.floor == 2:

            result_floor = floor2(player, monster)

            player.level_up()

            player.update_stats()

            if result_floor:

                win_message(dungeon, '2')


        if player.floor == 3:

            result_floor = floor3(player, monster)

            player.level_up()

            player.update_stats()

            if result_floor:

                win_message(dungeon, '3')

        if player.floor == 4:

            result_floor = floor4(player, monster)

            player.level_up()

            player.update_stats()

            if  result_floor:

                win_message(dungeon, '4')

        if player.floor == 5:

            result_floor = floor5(player, monster)

            player.level_up()

            player.update_stats()

            if  result_floor:

                win_message(dungeon, '5')

        if player.floor == 6:

            result_floor = floor6(player, monster)

            player.level_up()

            player.update_stats()

            if result_floor:

                win_message(dungeon, '6')

        if player.floor == 7:

            result_floor = floor7(player, monster)

            player.level_up()

            player.update_stats()

            if result_floor:

                win_message(dungeon, '7')

        if player.floor == 8:

            result_floor = floor8(player, monster)

            player.level_up()

            player.update_stats()

            if result_floor:

                win_message(dungeon, '8')

        if player.floor == 9:

            result_floor = floor9(player, monster)

            player.level_up()

            player.update_stats()

            if result_floor:

                win_message(dungeon, '9')

        if player.floor == 10:

            result_floor = floor10(player, monster, monster)

            player.level_up()

            player.update_stats()

            if result_floor:

                win_message(dungeon, '10')

                win = True

        if not result_floor: return False

    return True
        
def dungeon1(player: MainCharacter) -> bool:

    # INTRODUÇÃO A DUNGEON

    if player.floor < 3:

        dungeon_decorator('Dungeon 1')

        animated_text(f'Voz Desconhecida: Olá {player.name}, sou Isabely e serei sua guia nesta jornada.\nQuando você finalizar a primeira dungeon poderei te explicar sobre como usar\nas habilidades que você irá despertar no caminho. Se você conseguir finalizar\na dungeon, é claro. Desejo-lhe boa sorte.')

        animated_text(input('\n\n\033[1;33mPressione enter para continuar...\033[m'))

        dungeon_decorator('Dungeon 1')

        animated_text(f'\033[1;35mIsabely\033[m: A primeira dungeon foi dominada pelos slimes, cada Dungeon tem\n10 andares, você tera que limpar cada um deles para poder finaliza-la.')

        animated_text(input('\n\n\033[1;33mPressione enter para continuar...\033[m'))
    
    result = dungeon('Dungeon 1', player, ['slime'])
        
    return result
        
def dungeon2(player: MainCharacter) -> bool:

    # INTRODUÇÃO A DUNGEON

    if player.floor < 3:

        dungeon_decorator('Dungeon 2')
    
    result = dungeon('Dungeon 2', player, ['goblin'])
        
    return result
        
def dungeon3(player: MainCharacter) -> bool:

    # INTRODUÇÃO A DUNGEON

    if player.floor < 3:

        dungeon_decorator('Dungeon 3')
    
    result = dungeon('Dungeon 3', player, ['esqueleto'])
        
    return result
        
def dungeon4(player: MainCharacter) -> bool:

    # INTRODUÇÃO A DUNGEON

    if player.floor < 3:

        dungeon_decorator('Dungeon 4')
    
    result = dungeon('Dungeon 4', player, ['orc'])
        
    return result
        
def dungeon5(player: MainCharacter) -> bool:

    # INTRODUÇÃO A DUNGEON

    if player.floor < 3:

        dungeon_decorator('Dungeon 5')
    
    result = dungeon('Dungeon 5', player, ['slime', 'goblin', 'esqueleto', 'orc'])
        
    return result
