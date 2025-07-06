from code.Enemy import Enemy
from code.Player import Player
from code.constants import PATH_BG, SCREEN_HEIGHT, SCREEN_WIDTH


class FactoryEntity:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Player':
                return Player('Player', 40, 53,
                              [10, SCREEN_HEIGHT - 200], PATH_BG[f'{entity_name}_idle'], 54, 76)
            case 'Enemy1':
                return Enemy('Enemy1', 40, 53,
                              [SCREEN_WIDTH - 100, SCREEN_HEIGHT - 200], PATH_BG[f'{entity_name}_idle'], 54, 76)
        return None
