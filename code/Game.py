import pygame

from code.Menu import Menu
from code.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True

    def run(self):
        pygame.display.set_caption('Shinobi Attack')
        while self.running:
            menu = Menu(self.screen)
            menu.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()
        quit()
