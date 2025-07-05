import pygame.base
from pygame import display, event, constants

from code.Level import Level
from code.Menu import Menu
from code.constants import SCREEN_WIDTH, SCREEN_HEIGHT, MENU_OPTION


class Game:
    def __init__(self):
        pygame.base.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True

    def run(self):
        pygame.display.set_caption('Shinobi Attack')
        while self.running:
            menu = Menu(self.screen)
            result = menu.run()

            if result == MENU_OPTION[0]:
                level = Level(self.screen, 'level1Bg')
                level.run()
            elif result == MENU_OPTION[2]:
                self.running = False

            for events in pygame.event.get():
                if events.type == pygame.constants.QUIT:
                    self.running = False

        pygame.display.quit()
        quit()
