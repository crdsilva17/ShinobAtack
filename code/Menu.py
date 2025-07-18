import sys

import pygame.mixer_music
import pygame.draw
from pygame import transform, image, display, event, font
from pygame.constants import *
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.constants import *


class Menu:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.surf = transform.scale(image.load(PATH_BG['MenuBg']).convert_alpha(),
                                    (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.surf.get_rect()

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('assets/sound/menu2.mp3')
        pygame.mixer_music.play(-1)
        running = True
        while running:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(TEXT_BIG, "SHINOBI ATTACK", COLOR_RED, (SCREEN_CENTER, 120))
            pygame.draw.rect(self.screen, COLOR_BLACK, (900, 150, 200, 200))
            self.menu_text(TEXT_SMALL,'Este é um Jogo demo',COLOR_YELLOW, (1000, 200))
            self.menu_text(TEXT_SMALL,'Movimentação [<-] [->]',COLOR_YELLOW, (1000, 230))
            self.menu_text(TEXT_SMALL,'Ataque 1 [LCTRL]',COLOR_YELLOW, (1000, 260))
            self.menu_text(TEXT_SMALL,'Ataque 2 [LALT]',COLOR_YELLOW, (1000, 290))


            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(TEXT_MEDIUM, MENU_OPTION[i], COLOR_BLUE, (SCREEN_CENTER, 400 + 30 * i))
                else:
                    self.menu_text(TEXT_MEDIUM, MENU_OPTION[i], COLOR_WHITE, (SCREEN_CENTER, 400 + 30 * i))

            for events in event.get():
                if events.type == QUIT:
                    running = False
                if events.type == KEYDOWN:
                    if events.key == K_DOWN:
                        menu_option = menu_option + 1 if menu_option < len(MENU_OPTION) - 1 else 0
                    elif events.key == K_UP:
                        menu_option = menu_option - 1 if menu_option > 0 else len(MENU_OPTION) - 1
                    elif events.key == K_RETURN:
                        return MENU_OPTION[menu_option]

            display.flip()
        display.quit()
        sys.exit(0)

    def menu_text(self, size: int, text: str, color: tuple, position: tuple):
        text_font: Font = font.SysFont(name='Arial', size=size)
        text_surf: Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=position)
        self.screen.blit(text_surf, text_rect)
