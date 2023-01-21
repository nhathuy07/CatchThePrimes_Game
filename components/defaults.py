import pygame
from pathlib import Path
from enum import Enum
pygame.mixer.init()
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

MAINMENU_BGM = Path("assets/Audio/melancholy-sad-guitar-ambient.wav")
IN_GAME_BGM = Path("assets/Audio/repose-travel-ambient-piano-future-bass.wav")

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

# Effects
SFX_CLICK = pygame.mixer.Sound(Path("assets/Audio/mixkit-video-game-mystery-alert-234.wav"))
SFX_HIT = pygame.mixer.Sound(Path("assets/Audio/zapsplat_multimedia_game_sound_ping_beep_high_pitched_point_earned_or_correct_answer_positive_78345.wav"))
SFX_MISS = pygame.mixer.Sound(Path("assets/Audio/zapsplat_multimedia_game_error_tone_006_24924.wav"))
SFX_TIME_RUNNING_OUT = pygame.mixer.Sound(Path("assets/Audio/zapsplat_game_sound_timer_click_plastic_steady_slow_72191.wav"))
SFX_TIME_UP = pygame.mixer.Sound(Path("assets/Audio/zapsplat_multimedia_game_sound_bell_ping_ring_time_up_78300.wav"))

SFX_TIME_UP.set_volume(1.0)