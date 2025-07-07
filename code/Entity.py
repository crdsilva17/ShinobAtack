from abc import ABC, abstractmethod

from pygame.surface import Surface


class Entity(ABC):
    def __init__(self, name: str, wx: int, wy: int, path: str, w: int, h: int):
        self.name = name
        self.sprite_sheet = None
        self.path = path
        self.speed = 0
        self.wx = wx
        self.wy = wy
        self.w = w
        self.h = h
        self.direction = 0
        self.health = 50
        self.health_limit = None
        self.action_type = 0
        self.action = False
        self.action_timer = 0
        self.action_frame_delay = 1
        self.action_frame_index = 0
        self.action_sequence = []
        self.attack_range = 40
        self.entity_type = "neutral"

    @abstractmethod
    def update(self, surface:Surface):
        pass

    @abstractmethod
    def action_update(self):
        pass

    @abstractmethod
    def draw(self, surface, img, wxy:tuple, pos:tuple, size:tuple):
        pass

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
    def action_start(self, action_type=0):
        pass

    @abstractmethod
    def damage(self, amount: int):
        pass

    @abstractmethod
    def entity_text(self, *args, **kwargs):
        pass
