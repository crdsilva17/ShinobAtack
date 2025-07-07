import math
import random

import pygame
import pygame.mixer_music
from pygame import draw, font, image, transform
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Entity import Entity
from code.constants import COLOR_GREEN, COLOR_YELLOW, COLOR_RED, HEALTH, SCREEN_WIDTH, PATH_BG


class Enemy(Entity):
    def __init__(self, name: str, wx: int, wy: int, position: list[int], path: str, w: int, h: int,
                 game_mediator):
        super().__init__(name, wx, wy, path, w, h)
        self.name = name
        self.wx = wx
        self.wy = wy
        self.w = w
        self.h = h
        self.path = path
        self.speed = random.randint(2, 15)
        self.run_step = 0
        self.dir = random.choice([0, 1])  # 0 = direita, 1 = esquerda
        self.patrol_timer = 0
        self.patrol_delay = 60
        self.map_limit = (0, SCREEN_WIDTH)  # (x_min, x_max)
        self.atck = 0
        self.type_attack = 0
        self.position = position
        self.health_limit = HEALTH[name] * 0.8
        self.health = HEALTH[self.name]
        self.game_mediator = game_mediator
        self.game_mediator.add_enemy(self)
        self.attack_range = 40
        self.attacking = False
        self.entity_type = "enemy"

    def move(self):
        run = [5, 137, 266, 395, 520, 650, 776, 905]
        self.w = 65
        player_pos = self.game_mediator.get_player_position()
        self.surf = image.load(PATH_BG[f'{self.name}_idle']).convert_alpha()
        if self.dir == 1:
            self.surf = transform.flip(self.surf, True, False)
        distance = math.hypot(player_pos[0] - self.position[0], 0) if player_pos else float('inf')
        distance_max = 500

        if player_pos and distance <= distance_max:
            # Perseguir o player no eixo X
            if player_pos[0] - self.position[0] > 30:
                self.surf = image.load(PATH_BG[f'{self.name}_run']).convert_alpha()
                self.dir = 0  # direita
                self.position[0] += self.speed
                self.wx = run[self.run_step]
                self.run_step += 1
                if self.run_step >= len(run) - 1:
                    self.run_step = 0
            elif self.position[0] - player_pos[0] > 30:
                self.surf = image.load(PATH_BG[f'{self.name}_run']).convert_alpha()
                self.surf = transform.flip(self.surf, True, False)
                self.dir = 1  # esquerda
                self.position[0] -= self.speed
                self.wx = run[self.run_step] + 55  # Constantante para compensar o flip da imagem
                self.run_step -= 1
                if self.run_step <= 0:
                    self.run_step = len(run) - 1
            else:
                self.attack()
        else:
            # Movimento aleatório (patrulha)
            self.patrol_timer += 1

            if self.patrol_timer >= self.patrol_delay:
                self.dir = random.choice([0, 1])  # nova direção aleatória
                self.patrol_timer = 0
            if self.dir == 0:
                self.position[0] += self.speed * 0.5
                self.surf = image.load(PATH_BG[f'{self.name}_walk']).convert_alpha()
                self.wx = run[self.run_step]
                self.run_step += 1
                if self.run_step >= len(run) - 1:
                    self.run_step = 0
            else:
                self.position[0] -= self.speed * 0.5
                self.surf = image.load(PATH_BG[f'{self.name}_walk']).convert_alpha()
                self.surf = transform.flip(self.surf, True, False)
                self.wx = run[self.run_step] + 55  # Constantante para compensar o flip da imagem
                self.run_step -= 1
                if self.run_step <= 0:
                    self.run_step = len(run) - 1
            if self.position[0] <= self.map_limit[0]:
                self.position[0] = self.map_limit[0]
                self.dir = 0
            elif self.position[0] >= self.map_limit[1]:
                self.position[0] = self.map_limit[1]
                self.dir = 1

    def attack(self):
        self.w = 110
        attack_one = [22, 149, 273, 400]
        self.surf = image.load(PATH_BG[f'{self.name}_attack1']).convert_alpha()
        if self.atck == 2:
            self.attacking = True
        else:
            self.attacking = False
        if self.dir > 0:
            self.surf = transform.flip(self.surf, True, False)
            self.wx = attack_one[self.atck] - (30 if self.type_attack == 1 else 20)
            self.atck -= 1
            if self.atck <= 0:
                self.atck = len(attack_one) - 1
        else:
            self.wx = attack_one[self.atck]
            self.atck += 1
            if self.atck >= len(attack_one) - 1:
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
        pygame.mixer_music.load('assets/sound/attack2.wav')
        pygame.mixer_music.play()

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
