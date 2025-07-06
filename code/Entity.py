from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, wx: int, wy: int, path: str, w: int, h: int):
        self.name = name
        self.surf = pygame.image.load(path).convert_alpha()
        # self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.wx = wx
        self.wy = wy
        self.w = w
        self.h = h
        self.health = None
        self.attack_range = None
        self.attacking = False
        self.entity_type = "neutral"

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def get_pos(self):
        pass

    @abstractmethod
    def life_rect(self, *args, **kwargs):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def damage(self, amount: int):
        pass

    @abstractmethod
    def entity_text(self, *args, **kwargs):
        pass
