from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, wx: int, wy: int, position: list[int], path: str):
        self.name = name
        self.surf = pygame.image.load(path).convert_alpha()
        # self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.wx = wx
        self.wy = wy
        self.position = position

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def get_pos(self):
        pass

    @abstractmethod
    def life_rect(self, screen, health: int, position: tuple):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def damage(self, receive: int):
        pass

    @abstractmethod
    def entity_text(self, screen, size: int, text: str, color: tuple, position: tuple):
        pass
