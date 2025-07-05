from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple, path: str):
        self.name = name
        self.surf = pygame.image.load(path + name + '.png')
        self.rect = self.surf.get_rect(position[0], position[1])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass

