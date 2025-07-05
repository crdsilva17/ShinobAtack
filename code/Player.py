from pygame import draw, font, key, image, transform
from pygame.constants import K_RIGHT, K_LEFT
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Entity import Entity
from code.constants import COLOR_GREEN, COLOR_YELLOW, COLOR_RED, SCREEN_WIDTH, PATH_BG


class Player(Entity):
    def __init__(self, name: str, wx: int, wy: int, position: list[int], path: str):
        super().__init__(name, wx, wy, position, path)
        self.name = name
        self.wx = wx
        self.wy = wy
        self.position = position
        self.path = path
        self.speed = 10
        self.run_step = 0

    def move(self):
        run = [13, 142, 269, 396, 523, 650, 777, 904]  # Vetor para implementar animações

        key_pressed = key.get_pressed()
        if key_pressed[K_RIGHT] and self.position[0] < SCREEN_WIDTH - 50:
            self.surf = image.load(PATH_BG[3]).convert_alpha()  # Carregar imagem correndo
            self.position[0] += 1 * self.speed
            self.wx = run[self.run_step]
            self.run_step += 1
            if self.run_step >= len(run) - 1:
                self.run_step = 0

        elif key_pressed[K_LEFT] and self.position[0] > 0:
            self.surf = image.load(PATH_BG[3]).convert_alpha()
            self.surf = transform.flip(self.surf, True, False)  # Espelhar imagem
            self.position[0] -= 1 * self.speed
            self.wx = run[self.run_step] + 52  # Constantante para compensar o flip da imagem
            self.run_step -= 1
            if self.run_step <= 0:
                self.run_step = len(run) - 1
        else:
            self.run_step = 0
            self.surf = image.load(PATH_BG[2]).convert_alpha()
            self.wx = 40

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
