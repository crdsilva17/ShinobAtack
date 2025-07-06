import pygame.surface
from pygame import display, image, transform, event, constants, time, font
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Entity import Entity
from code.EntityFactory import *
from code.constants import PATH_BG, SCREEN_WIDTH, SCREEN_HEIGHT, TEXT_SMALL, COLOR_WHITE, HEALTH, COLOR_BLACK


class Level:
    def __init__(self, screen: Surface, name: str):
        self.screen = screen
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.append(FactoryEntity.get_entity('Player'))
        self.entity_list.append(FactoryEntity.get_entity('Enemy1'))

    def run(self):
        # pygame.mixer_music.load('')
        # pygame.mixer_music.play(-1)
        clock_fps = time.Clock()
        player_score = 0
        while True:
            clock_fps.tick(60)
            if self.name == 'level1Bg':
                surf_bg = transform.scale(image.load(PATH_BG[self.name]), (SCREEN_WIDTH, SCREEN_HEIGHT))
                rect = surf_bg.get_rect()
                self.screen.blit(source=surf_bg, dest=rect)

                for ent in self.entity_list:
                    self.level_blit(ent.surf, (ent.wx, ent.wy), ent.get_pos(), (ent.w, ent.h))
                    ent.entity_text(self.screen, TEXT_SMALL, ent.name, COLOR_BLACK,
                                    (ent.get_pos()[0] + 50, ent.get_pos()[1] - 40))
                    ent.life_rect(self.screen, HEALTH[ent.name], (ent.get_pos()[0], ent.get_pos()[1] - 20))
                    ent.move()


            for events in event.get():
                if events.type == constants.QUIT:
                    display.quit()
                    quit(0)
            self.level_text(TEXT_SMALL, f'Level 1 - SCORE: {player_score}', COLOR_WHITE, (10, 20))

            display.flip()

    def level_text(self, size: int, text: str, color: tuple, position: tuple):
        text_font: Font = font.SysFont(name='Arial', size=size)
        text_surf: Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=position[0], top=position[1])
        self.screen.blit(text_surf, text_rect)

    def level_blit(self, img, wxy:tuple, pos:tuple, size:tuple):
        surf = pygame.surface.Surface(size).convert()
        surf.blit(img, (0,0), (wxy, size ))
        alpha = surf.get_at((0, 0))
        surf.set_colorkey(alpha)
        self.screen.blit(surf, pos)