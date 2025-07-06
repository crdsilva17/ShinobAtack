import random

from code.Enemy import Enemy
from code.Player import Player
from code.constants import PATH_BG, SCREEN_HEIGHT, SCREEN_WIDTH


class FactoryEntity:
    @staticmethod
    def get_entity(entity_name: str, game_mediator):
        match entity_name:
            case 'Player':
                player = Player('Player', 40, 53,
                                [10, SCREEN_HEIGHT - 200], PATH_BG[f'{entity_name}_idle'], 54, 76)
                game_mediator.register_player(player)
                return player
            case 'Enemy1':
                return Enemy('Enemy1', 40, 53,
                             [SCREEN_WIDTH - random.randint(50, 100),
                              SCREEN_HEIGHT - 200], PATH_BG[f'{entity_name}_idle'],65, 95, game_mediator)
        return None
