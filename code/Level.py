from pygame.surface import Surface

from code.Entity import Entity


class Level:
    def __init__(self, screen: Surface, name: str):
        self.screen = screen
        self.name = name
        self.list_entity : list[Entity] = []

    def run(self):
        pass
