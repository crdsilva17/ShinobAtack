from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name: str, position: list[int]):
        self.name = name
        self.position = position


    @abstractmethod
    def damage(self, amount: int):
        pass

