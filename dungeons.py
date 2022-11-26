from floors import d1_floor1
from utils import animated_text, clean, text_decorator


def dungeon_decorator(dungeon):

    clean()

    text_decorator(f'         {dungeon}         ', color='cian')


def dungeon1(player):

    # INTRODUÇÃO A DUNGEON

    dungeon_decorator('Dungeon 1')

    animated_text(f'Voz Desconhecida: Olá {player.name}, sou Isabely e serei sua guia nesta jornada.\nQuando você finaliza-la poderei te explicar sobre como usar as habilidades que\nvocê irá despertar no caminho. Se você conseguir finalizar a dungeon, é claro.\nDesejo-lhe boa sorte em sua primeira dungeon.')

    input('\n\nPressione enter para continuar...')

    dungeon_decorator('Dungeon 1')

    animated_text(f'\033[1;35mIsabely\033[m: A primeira dungeon foi dominada pelos slimes, cada Dungeon tem\n10 andares, você tera que limpar cada um deles para poder finaliza-la.')

    input('\n\nPressione enter para continuar...')
    
    d1_floor1(player)
    
    dungeon_decorator('Dungeon 1')

    animated_text(f'Parabéns! você limpou com sucesso o primeiro andar da Dungeon 1')

    print()

    animated_text(input('Pressione enter para prosseguir...'))

