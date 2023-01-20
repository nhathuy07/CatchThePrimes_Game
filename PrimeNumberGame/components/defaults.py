import pygame
from pathlib import Path
from enum import Enum
pygame.font.init()
DEFAULT_MAINMENU_ELEM_VEL = 115
DEFAULT_MIN_SPEED = 0.2
DEFAULT_ALPHA_CHANGE_RATE = 4.5
DEFAULT_FONT_3DIG = pygame.font.Font(Path("assets/fonts/yoster.ttf"), 24)
DEFAULT_FONT_2DIG = pygame.font.Font(Path("assets/fonts/yoster.ttf"), 36)
DEFAULT_FONT_SMALL = pygame.font.Font(Path("assets/fonts/yoster.ttf"), 22)
F_COLORS = ((102, 86, 0), (242, 204, 255), (92, 0, 82))
class Graphics:
    DEFAULT_PARTICLE = pygame.image.load(Path("assets/Particle.png"))
    STAR_PARTICLE = pygame.image.load(Path("assets/star_particle.png"))

class Screens(Enum):
    MAIN_MENU = 101
    INSTRUCTION = 102
    PLAY = 103

class ParticleModes(Enum):
    NORM = 201
    BURST = 202

GO_TO_MAINMENU = pygame.event.Event(pygame.USEREVENT + 1)
GO_TO_INSTRUCTION = pygame.event.Event(pygame.USEREVENT + 2)
PLAY = pygame.event.Event(pygame.USEREVENT + 3)
PAUSE = pygame.event.Event(pygame.USEREVENT + 4)
TIMER_COLOR = (133, 105, 180)
TIMER_WARNING_COLOR = (180, 105, 105)

# buttons
MB_OK = 0x0
MB_OKCXL = 0x01
MB_YESNOCXL = 0x03
MB_YESNO = 0x04
MB_HELP = 0x4000

# icons
ICON_EXCLAIM = 0x30
ICON_INFO = 0x40
ICON_STOP = 0x10