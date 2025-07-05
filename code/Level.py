from pygame import display, image, transform, event, constants
from pygame.constants import KEYDOWN
from pygame.surface import Surface

from code.Entity import Entity
from code.constants import PATH_BG, SCREEN_WIDTH, SCREEN_HEIGHT


class Level:
    def __init__(self, screen: Surface, name: str):
        self.screen = screen
        self.name = name
        self.entity_list: list[Entity] = []

    def run(self):
        while True:
            if self.name == 'level1Bg':
                surf_bg = transform.scale(image.load(PATH_BG[1]), (SCREEN_WIDTH, SCREEN_HEIGHT))
                rect = surf_bg.get_rect()
                self.screen.blit(source=surf_bg, dest=rect)

            for events in   event.get():
                if events.type == constants.QUIT:
                    display.quit()
                    quit(0)

            display.flip()
