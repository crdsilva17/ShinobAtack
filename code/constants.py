# C
import pygame.constants

COLOR_RED = (203, 4, 4)
COLOR_GREEN = (4, 203, 4)
COLOR_BLUE = (4, 4, 203)
COLOR_ORANGE = (255, 159, 0)
COLOR_TEAL = (48, 152, 152)
COLOR_YELLOW = (255, 214, 107)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

# D
DAMAGE = ({
    'Player': 10,
    'Enemy1': 4,
    'Enemy2': 1,
    'Enemy3': 2
})

# E
ENEMY_MAX = 50
EVENT_ENEMY = pygame.constants.USEREVENT + 1
ENEMY_TIME = 1000

# H
HEALTH = ({
    'Player': 100,
    'Enemy1': 30,
    'Enemy2': 50,
    'Enemy3': 40
})
HEALTH_POS = ({
    'Player': 20,
    'Enemy1': 0
})

# M
MENU_OPTION = (
    'NEW_GAME',
    'SCORE',
    'EXIT'
)

# P
PATH_BG = ({
    'MenuBg': 'assets/fantasy-2d-battlegrounds/PNG/Battleground1/Bright/Battleground1.png',
    'level1Bg': 'assets/fantasy-2d-battlegrounds/PNG/Battleground2/Bright/Battleground2.png',
    'Player_idle': 'assets/shinob-sprites/Samurai/Idle.png',
    'Player_run': 'assets/shinob-sprites/Samurai/Run.png',
    'Player_attack1': 'assets/shinob-sprites/Samurai/Attack_1.png',
    'Player_attack2': 'assets/shinob-sprites/Samurai/Attack_2.png',
    'Enemy1_idle': 'assets/samurai-sprite/Samurai_Commander/Idle.png',
    'Enemy1_run': 'assets/samurai-sprite/Samurai_Commander/Run.png',
    'Enemy1_walk': 'assets/samurai-sprite/Samurai_Commander/Walk.png',
    'Enemy1_attack1': 'assets/samurai-sprite/Samurai_Commander/Attack_1.png'
})

# S
SCREEN_WIDTH = 1220
SCREEN_HEIGHT = 600
SCREEN_CENTER = SCREEN_WIDTH / 2

# T
TEXT_BIG = 60
TEXT_MEDIUM = 28
TEXT_SMALL = 20
TEXT_POS = ({
    'Player': 40,
    'Enemy1': 20
})
