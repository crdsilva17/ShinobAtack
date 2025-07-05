import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.constants import *


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pygame.transform.scale(pygame.image.load('assets/fantasy-2d-battlegrounds/'
                                                             'PNG/Battleground1/Bright/'
                                                             'Battleground1.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.surf.get_rect()

    def run(self):
        # pygame.mixer_music.load('')
        # pygame.mixer_music.play(-1)
        while True:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(TEXT_BIG, "SHINOBI ATTACK", COLOR_RED, (SCREEN_CENTER, 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(TEXT_MEDIUM, MENU_OPTION[i], COLOR_WHITE, (SCREEN_CENTER, 400 + 30 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, size: int, text: str, color: tuple, position: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=size)
        text_surf: Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=position)
        self.screen.blit(text_surf, text_rect)
