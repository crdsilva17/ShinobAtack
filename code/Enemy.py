from pygame import draw, font
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Entity import Entity
from code.Player import Player
from code.constants import COLOR_GREEN, COLOR_YELLOW, COLOR_RED, HEALTH


class Enemy(Entity):
    def __init__(self, name: str, wx: int, wy: int, position: list[int], path: str, w: int, h: int):
        super().__init__(name, wx, wy, path, w, h)
        self.name = name
        self.wx = wx
        self.wy = wy
        self.w = w
        self.h = h
        self.path = path
        self.speed = 5
        self.run_step = 0
        self.dir = 0
        self.atck = 0
        self.type_attack = 0
        self.position = position
        self.health_limit = HEALTH[name] * 0.8

    def move(self):
        pass

    def attack(self):
        pass

    def damage(self, receive: int):
        pass

    def get_pos(self):
        return self.position

    def life_rect(self, screen, health: int, position: tuple):
        if health > self.health_limit:
            draw.rect(screen, COLOR_GREEN, (position[0], position[1], health, 5))
        elif self.health_limit >= health > self.health_limit * 0.5:
            draw.rect(screen, COLOR_YELLOW, (position[0], position[1], health, 5))
        else:
            draw.rect(screen, COLOR_RED, (position[0], position[1], health, 5))

    def entity_text(self, screen, size: int, text: str, color: tuple, position: tuple):
        text_font: Font = font.SysFont(name='Arial', size=size)
        text_surf: Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=position)
        screen.blit(text_surf, text_rect)
