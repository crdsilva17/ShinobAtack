import math
import random

import pygame
import pygame.image
import pygame.mixer
import pygame.mixer_music
from pygame import draw, font, transform
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Entity import Entity
from code.constants import COLOR_GREEN, COLOR_YELLOW, COLOR_RED, HEALTH, SCREEN_WIDTH, PATH_BG


class Enemy(Entity):
    def __init__(self, name: str, wx: int, wy: int, position: list[int], path: str, w: int, h: int,
                 game_mediator):
        super().__init__(name, wx, wy, path, w, h)
        self.speed = random.randint(2, 8)
        self.direction = random.choice([0, 1])
        self.patrol_timer = 0
        self.patrol_delay = 60
        self.map_limit = (0, SCREEN_WIDTH)  # (x_min, x_max)
        self.position = position
        self.health_limit = HEALTH[name] * 0.8
        self.health = HEALTH[self.name]
        self.game_mediator = game_mediator
        self.game_mediator.add_enemy(self)
        self.entity_type = "enemy"

    def move(self):
        player_pos = self.game_mediator.get_player_position()
        distance = math.hypot(player_pos[0] - self.position[0], 0) if player_pos else float('inf')
        distance_max = 500

        if player_pos and distance <= distance_max:

            if player_pos[0] - self.position[0] > 30:
                self.action_start(3)
                self.direction = 0
                self.position[0] += self.speed
            elif self.position[0] - player_pos[0] > 30:
                self.action_start(3)
                self.direction = 1
                self.position[0] -= self.speed
            else:
                self.action_start(0)
        else:
            self.patrol_timer += 1
            self.action_start(2)
            if self.patrol_timer >= self.patrol_delay:
                self.direction = random.choice([0, 1])  # new random direction
                self.patrol_timer = 0
            if self.direction == 0:
                self.position[0] += self.speed * 0.5
            else:
                self.position[0] -= self.speed * 0.5
            if self.position[0] <= self.map_limit[0]:
                self.position[0] = self.map_limit[0]
                self.direction = 0
            elif self.position[0] >= self.map_limit[1]:
                self.position[0] = self.map_limit[1]
                self.direction = 1

    def update(self, surface: Surface):
        self.move()
        self.action_update()
        self.draw(surface, self.sprite_sheet, (self.wx, self.wy),
                  (self.get_pos()[0], self.get_pos()[1]), (self.w, self.h))

    def action_update(self):
        if self.action_type > 1:
            self.w = 65
        else:
            self.w = 110

        if not self.action:
            self.sprite_sheet = pygame.image.load(PATH_BG[f'{self.name}_idle']).convert_alpha()
            return
        self.action_timer += 1
        if self.action_timer >= self.action_frame_delay:
            self.action_timer = 0
            self.action_frame_index += 1
            if self.action_frame_index >= len(self.action_sequence):
                self.action_frame_index = 0
                self.action = False
                return

        if self.direction == 0:
            self.action_sequence.sort(reverse=False)
        else:
            self.action_sequence.sort(reverse=True)
        frame = self.action_sequence[self.action_frame_index]

        if self.action_type < 2:
            self.sprite_sheet = pygame.image.load(PATH_BG[f'{self.name}_attack{1 + self.action_type}']).convert_alpha()
        elif self.action_type == 2:
            self.sprite_sheet = pygame.image.load(PATH_BG[f'{self.name}_walk']).convert_alpha()
        else:
            self.sprite_sheet = pygame.image.load(PATH_BG[f'{self.name}_run']).convert_alpha()

        if self.direction > 0:
            self.sprite_sheet = transform.flip(self.sprite_sheet, True, False)
            self.wx = frame + (55 if self.action_type > 1 else -20)
        else:
            self.wx = frame

    def draw(self, surface, img, wxy: tuple, pos: tuple, size: tuple):
        surf = pygame.surface.Surface(size).convert()
        surf.blit(img, (0, 0), (wxy, size))
        alpha = surf.get_at((0, 0))
        surf.set_colorkey(alpha)
        surface.blit(surf, pos)

    def action_start(self, action_type=0):
        if not self.action:
            self.action_type = action_type
            self.action_frame_index = 0
            self.action_timer = 0
            self.action = True
            if action_type < 2:
                self.attacking = True
                hit_sound = pygame.mixer.Sound('assets/sound/attack.wav')
                sword_sound = pygame.mixer.Sound('assets/sound/attack2.wav')
                hit_sound.play()
                sword_sound.play()
                hit_sound.set_volume(0.4)
                sword_sound.set_volume(0.4)
            else:
                self.attacking = False
            if action_type == 0:
                self.action_sequence = [22, 149, 273, 400]
            elif action_type == 1:
                self.action_sequence = [22, 149, 273, 400]
            else:
                self.action_sequence = [5, 137, 266, 395, 520, 650]

    def get_rect(self):
        return pygame.rect.Rect(self.position[0], self.position[1], self.w, self.h)

    def get_attack_rect(self):
        if self.direction == 0:  # right
            return pygame.rect.Rect(
                self.position[0] + self.w,
                self.position[1],
                self.attack_range,
                self.h
            )
        else:  # left
            return pygame.rect.Rect(
                self.position[0] - self.attack_range,
                self.position[1],
                self.attack_range,
                self.h
            )

    def damage(self, amount: int):
        self.health -= amount

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
