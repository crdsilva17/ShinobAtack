from pygame import draw, font, key
from pygame.constants import K_RIGHT, K_LEFT
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Entity import Entity
from code.constants import COLOR_GREEN, COLOR_YELLOW, COLOR_RED, SCREEN_WIDTH


class Player(Entity):
    def __init__(self, name: str, position: list[int], path: str):
        super().__init__(name, position, path)
        self.name = name
        self.position = position
        self.path = path
        self.speed = 10

    def move(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_RIGHT] and self.position[0] < SCREEN_WIDTH - 50:
            self.position[0] += 1 * self.speed
        elif key_pressed[K_LEFT] and self.position[0] > 0:
            self.position[0] -= 1 * self.speed

    def attack(self):
        pass

    def damage(self, receive: int):
        pass

    def get_pos(self):
        return self.position

    def life_rect(self, screen, health: int, position: tuple):
        if health > 80:
            draw.rect(screen, COLOR_GREEN, (position[0], position[1], health, 5))
        elif 80 >= health > 30:
            draw.rect(screen, COLOR_YELLOW, (position[0], position[1], health, 5))
        else:
            draw.rect(screen, COLOR_RED, (position[0], position[1], health, 5))

    def entity_text(self, screen, size: int, text: str, color: tuple, position: tuple):
        text_font: Font = font.SysFont(name='Arial', size=size)
        text_surf: Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=position)
        screen.blit(text_surf, text_rect)
