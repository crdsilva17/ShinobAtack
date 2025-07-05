from code.Player import Player
from code.constants import PATH_BG, SCREEN_HEIGHT


class FactoryEntity:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Player':
                return Player('Player', 40, 53, [10, SCREEN_HEIGHT - 200], PATH_BG[2])
        return None
