from characters import MainCharacter
from floors import *
from utils import animated_text, clean, text_decorator


def dungeon_decorator(dungeon):

    clean()

    text_decorator(f'         {dungeon}         ', color='cian')

def win_message(dungeon):

        dungeon_decorator(dungeon)

        animated_text(f'Parabéns! você limpou com sucesso o primeiro andar da Dungeon 1')

        animated_text(input('\n\n\033[1;33mPressione enter para prosseguir para o proxímo andar...\033[m'))

def dungeon1(player: MainCharacter) -> bool:

    # INTRODUÇÃO A DUNGEON

    if player.floor < 3:

        dungeon_decorator('Dungeon 1')

        animated_text(f'Voz Desconhecida: Olá {player.name}, sou Isabely e serei sua guia nesta jornada.\nQuando você finalizar a primeira dungeon poderei te explicar sobre como usar\nas habilidades que você irá despertar no caminho. Se você conseguir finalizar\na dungeon, é claro. Desejo-lhe boa sorte.')

        animated_text(input('\n\n\033[1;33mPressione enter para continuar...\033[m'))

        dungeon_decorator('Dungeon 1')

        animated_text(f'\033[1;35mIsabely\033[m: A primeira dungeon foi dominada pelos slimes, cada Dungeon tem\n10 andares, você tera que limpar cada um deles para poder finaliza-la.')

        animated_text(input('\n\n\033[1;33mPressione enter para continuar...\033[m'))
    
    win = False
    result_floor = False

    while not win: 
    
        if player.floor == 1:
        
            result_floor = floor1(player, 'slime')

            player.level_up()
            
            player.update_stats()

            if result_floor:

                win_message('Dungeon 1')

        if player.floor == 2:

            result_floor = floor2(player, 'slime')

            player.level_up()

            player.update_stats()

            if result_floor:

                win_message('Dungeon 2')


        if player.floor == 3:

            result_floor = floor3(player, 'slime')

            player.level_up()

            player.update_stats()

            if result_floor:

                win_message('Dungeon 3')

        if player.floor == 4:

            result_floor = floor4(player, 'slime')

            player.level_up()

            player.update_stats()

            if  result_floor:

                win_message('Dungeon 4')

        if player.floor == 5:

            result_floor = floor5(player, 'slime')

            player.level_up()

            player.update_stats()

            if  result_floor:

                win_message('Dungeon 5')

        if player.floor == 6:

            result_floor = floor6(player, 'slime')

            player.level_up()

            player.update_stats()

            if result_floor:

                win_message('Dungeon 6')

        if player.floor == 7:

            result_floor = floor7(player, 'slime')

            player.level_up()

            player.update_stats()

            if result_floor:

                win_message('Dungeon 7')

        if player.floor == 8:

            result_floor = floor8(player, 'slime')

            player.level_up()

            player.update_stats()

            if result_floor:

                win_message('Dungeon 8')

        if player.floor == 9:

            result_floor = floor9(player, 'slime')

            player.level_up()

            player.update_stats()

            if result_floor:

                win_message('Dungeon 9')

        if player.floor == 10:

            result_floor = floor10(player, 'slime', 'slime')

            player.level_up()

            player.update_stats()

            if result_floor:

                win_message('Dungeon 10')

                win = True

        if not result_floor: return False

    return True
        
