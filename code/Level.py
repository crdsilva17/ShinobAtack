import pygame.mixer_music
import pygame.surface
from pygame import display, image, transform, event, constants, time, font, key
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Entity import Entity
from code.EntityFactory import *
from code.GameMediator import GameMediator
from code.constants import PATH_BG, SCREEN_WIDTH, SCREEN_HEIGHT, TEXT_SMALL, COLOR_WHITE, COLOR_BLACK, \
    ENEMY_MAX, EVENT_ENEMY, ENEMY_TIME, TEXT_POS, HEALTH_POS


class Level:
    def __init__(self, screen: Surface, name: str, player_score: int):
        self.screen = screen
        self.name = name
        self.player_score = player_score
        self.entity_list: list[Entity] = []
        self.game_mediator = GameMediator()
        self.entity_list.append(FactoryEntity.get_entity('Player', self.game_mediator))
        pygame.time.set_timer(EVENT_ENEMY, ENEMY_TIME)

    def run(self):
        pygame.mixer_music.load('assets/sound/level1.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.1)
        clock_fps = time.Clock()
        while True:
            clock_fps.tick(60)
            if self.name == 'level1Bg':
                surf_bg = transform.scale(image.load(PATH_BG[self.name]), (SCREEN_WIDTH, SCREEN_HEIGHT))
                rect = surf_bg.get_rect()
                self.screen.blit(source=surf_bg, dest=rect)

                for ent in self.entity_list:
                    ent.entity_text(self.screen, TEXT_SMALL, ent.name, COLOR_BLACK,
                                    (ent.get_pos()[0] + 50, ent.get_pos()[1] - TEXT_POS[ent.name]))
                    ent.life_rect(self.screen, ent.health,
                                  (ent.get_pos()[0], ent.get_pos()[1] - HEALTH_POS[ent.name]))
                    ent.update(self.screen)

                keys = key.get_pressed()
                if keys[constants.K_LCTRL]:
                    self.game_mediator.player.action_start(0)
                elif keys[constants.K_LALT]:
                    self.game_mediator.player.action_start(1)
                if keys[constants.K_RIGHT]:
                    self.game_mediator.player.action_start(2)
                if keys[constants.K_LEFT]:
                    self.game_mediator.player.action_start(3)


            # Aumentando dificuldade conforme Score
            match self.player_score:
                case 20:
                    self.game_mediator.player.attack_range = 40
                case 30:
                    self.game_mediator.player.attack_range = 30
                case 80:
                    self.game_mediator.player.attack_range = 20
                case 100:
                    self.game_mediator.player.attack_range = 10

            # Player ataca inimigos
            for enemy in self.game_mediator.enemies:
                self.game_mediator.check_attack(self.game_mediator.player, enemy)
                if enemy.health <= 0:
                    self.player_score += 1
                    self.game_mediator.destroy_enemy(enemy)
                    self.entity_list.remove(enemy)

            # Inimigos atacam o player
            for enemy in self.game_mediator.enemies:
                if self.game_mediator.player is None:
                    return self.player_score
                self.game_mediator.check_attack(enemy, self.game_mediator.player)
                self.game_mediator.player.attacking = False
                if self.game_mediator.player.health <= 0:
                    self.entity_list.remove(self.game_mediator.player)
                    self.game_mediator.remove_player()
            if self.game_mediator.player is None:
                return self.player_score

            for events in event.get():
                if events.type == constants.QUIT:
                    display.quit()
                    quit(0)
                if events.type == EVENT_ENEMY:
                    if self.game_mediator.count_enemies() < ENEMY_MAX:
                        self.entity_list.append(FactoryEntity.get_entity('Enemy1', self.game_mediator))

            self.level_text(TEXT_SMALL, f'Level 1 - SCORE: {self.player_score}', COLOR_WHITE, (10, 20))

            display.flip()

    def level_text(self, size: int, text: str, color: tuple, position: tuple):
        text_font: Font = font.SysFont(name='Arial', size=size)
        text_surf: Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=position[0], top=position[1])
        self.screen.blit(text_surf, text_rect)

