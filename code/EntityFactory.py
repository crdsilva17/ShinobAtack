from code.Background import Background
from code.constants import PATH_BG


class FactoryEntity:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                bg = Background('/Battleground2', position, PATH_BG[1])
                return bg
        return None
