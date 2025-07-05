from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple, path: str):
        super().__init__(name, position, path)

    def move(self):
        pass
