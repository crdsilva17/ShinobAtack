import pygame
from pygame import draw, font, key, image, transform
from pygame.constants import K_RIGHT, K_LEFT, K_LCTRL, K_LALT
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.Entity import Entity
from code.constants import COLOR_GREEN, COLOR_YELLOW, COLOR_RED, SCREEN_WIDTH, PATH_BG, HEALTH


class Player(Entity):
    def __init__(self, name: str, wx: int, wy: int, position: list[int], path: str, w: int, h: int):
        super().__init__(name, wx, wy, path, w, h)
        self.health_limit = HEALTH[name] * 0.8
        self.name = name
        self.wx = wx
        self.wy = wy
        self.w = w
        self.h = h
        self.position = position
        self.path = path
        self.speed = 10
        self.run_step = 0
        self.dir = 0
        self.atck = 0
        self.type_attack = 0
        self.health = HEALTH[self.name]
        self.attack_range = 60
        self.attacking = False
        self.entity_type = "player"

    def move(self):
        run = [13, 142, 269, 396, 523, 650, 777, 904]  # Vetor para implementar animações
        self.w = 54
        key_pressed = key.get_pressed()
        if key_pressed[K_RIGHT] and self.position[0] < SCREEN_WIDTH - 50:
            self.dir = 0
            self.surf = image.load(PATH_BG[f'{self.name}_run']).convert_alpha()  # Carregar imagem correndo
            self.position[0] += 1 * self.speed
            self.wx = run[self.run_step]
            self.run_step += 1
            if self.run_step >= len(run) - 1:
                self.run_step = 0

        elif key_pressed[K_LEFT] and self.position[0] > 0:
            self.surf = image.load(PATH_BG[f'{self.name}_run']).convert_alpha()
            self.surf = transform.flip(self.surf, True, False)  # Espelhar imagem
            self.dir = 1
            self.position[0] -= 1 * self.speed
            self.wx = run[self.run_step] + 52  # Constantante para compensar o flip da imagem
            self.run_step -= 1
            if self.run_step <= 0:
                self.run_step = len(run) - 1
        elif key_pressed[K_LCTRL]:
            self.type_attack = 0
            self.attack()
        elif key_pressed[K_LALT]:
            self.type_attack = 1
            self.attack()
        else:
            self.run_step = 0
            self.surf = image.load(PATH_BG[f'{self.name}_idle']).convert_alpha()
            if self.dir > 0:
                self.surf = transform.flip(self.surf, True, False)
            self.wx = 40

    def attack(self):
        self.w = 104
        attack_one = [22, 149, 276, 403, 530, 657]
        self.surf = image.load(PATH_BG[f'{self.name}_attack{1+self.type_attack}']).convert_alpha()  # Carregar imagem correndo
        if self.atck == 2:
            self.attacking = True
        else:
            self.attacking = False
        if self.dir > 0:
            self.surf = transform.flip(self.surf, True, False)
            self.wx = attack_one[self.atck] - (30 if self.type_attack == 1 else 20)
            self.atck -= 1
            if self.atck <= 0:
                self.atck = len(attack_one) - (1 if self.type_attack == 0 else 3)
        else:
            self.wx = attack_one[self.atck]
            self.atck += 1
            if self.atck >= len(attack_one) - (1 if self.type_attack == 0 else 3):
                self.atck = 0

    def get_rect(self):
        return pygame.rect.Rect(self.position[0], self.position[1], self.w, self.h)

    def get_attack_rect(self):
        """Calcula a área onde a espada atinge."""
        if self.dir == 0:  # direita
            return pygame.rect.Rect(
                self.position[0] + self.w,
                self.position[1],
                self.attack_range,
                self.h
            )
        else:  # esquerda
            return pygame.rect.Rect(
                self.position[0] - self.attack_range,
                self.position[1],
                self.attack_range,
                self.h
            )

    def damage(self, amount: int):
        self.health -= amount
        self.attacking = False
        print(f"{self.name} recebeu dano! Vida restante: {self.health}")

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
