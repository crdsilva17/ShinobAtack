from datetime import datetime

import pygame.display
import pygame.mixer_music
from pygame import transform, image, event, font
from pygame.constants import QUIT, K_RETURN, KEYDOWN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.DbProxy import DbProxy
from code.constants import PATH_BG, SCREEN_WIDTH, SCREEN_HEIGHT, TEXT_MEDIUM, SCORE_TEXT, COLOR_TEAL, \
    TEXT_SMALL, TEXT_BIG, COLOR_BLACK, COLOR_WHITE, COLOR_YELLOW, COLOR_RED


class Score:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.surf = transform.scale(image.load(PATH_BG['scoreBg']).convert_alpha(),
                                    (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.surf.get_rect()

    def save(self, score: int):
        pygame.mixer_music.load('assets/sound/score.mp3')
        pygame.mixer_music.play(-1)
        running = True
        db_proxy = DbProxy('DBScore')
        name = ''
        while running:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.score_text(TEXT_MEDIUM, 'YOU DEAD!', COLOR_RED, SCORE_TEXT['Title'])
            player_score = score
            text = 'Enter your name (4 character)'
            self.score_text(TEXT_SMALL, text, COLOR_WHITE, SCORE_TEXT['EnterName'])

            for events in event.get():
                if events.type == QUIT:
                    running = False
                elif events.type == KEYDOWN:
                    if events.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': player_score, 'date': get_formatted_date()})
                        db_proxy.close()
                        self.show()
                        return
                    elif events.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += events.unicode
            self.score_text(TEXT_SMALL, name, COLOR_TEAL, SCORE_TEXT['Name'])
            pygame.display.flip()

        pygame.display.quit()
        quit()

    def show(self):
        pygame.mixer_music.load('assets/sound/score.mp3')
        pygame.mixer_music.play(-1)
        self.screen.blit(source=self.surf, dest=self.rect)
        self.score_text(TEXT_BIG, 'TOP 10 SCORE', COLOR_RED, SCORE_TEXT['Title'])
        self.score_text(TEXT_MEDIUM, 'NAME                SCORE                 DATE',
                        COLOR_RED, SCORE_TEXT['Label'])
        db_proxy = DbProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(TEXT_MEDIUM, f'         {name}                   {score}               {date}',
                            COLOR_WHITE, SCORE_TEXT[list_score.index(player_score)])

        running = True
        while running:

            for events in event.get():
                if events.type == QUIT:
                    running = False
                if events.type == KEYDOWN:
                    if events.key == K_ESCAPE:
                        running = False
            pygame.display.flip()

        return

    def score_text(self, size: int, text: str, color: tuple, position: tuple):
        text_font: Font = font.SysFont(name='Arial', size=size)
        text_surf: Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=position)
        self.screen.blit(text_surf, text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_date} - {current_time}"
