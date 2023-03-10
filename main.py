import pygame
from components import ui
from components.defaults import Screens, GO_TO_MAINMENU, GO_TO_INSTRUCTION, PLAY, PAUSE, MB_YESNO, ICON_INFO, IN_GAME_BGM, MAINMENU_BGM
import ctypes

pygame.display.init()
pygame.mixer.init()


disp = pygame.display.set_mode(size=(860, 476), flags=pygame.SHOWN)
clock = pygame.time.Clock()

# Components
mainMenu = ui.MainMenu()
instructionScreen = ui.Instruction()
currentScreen = Screens.MAIN_MENU
gameplay = ui.Game()
#

pygame.mixer.music.load(MAINMENU_BGM)
pygame.mixer.music.play(fade_ms=350)
running = True
while running:
    if (currentScreen == Screens.MAIN_MENU):
        mainMenu.update(1/20)
        mainMenu.render(disp)
    elif (currentScreen == Screens.INSTRUCTION):
        instructionScreen.update()
        instructionScreen.render(disp)
    elif (currentScreen == Screens.PLAY):
        gameplay.update()
        gameplay.render(disp)
    
    for e in pygame.event.get():
        if (e.type == pygame.QUIT):
            exit(0)
        elif (e.type == GO_TO_INSTRUCTION.type):
            currentScreen = Screens.INSTRUCTION
        elif (e.type == PLAY.type):
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load(IN_GAME_BGM)
            pygame.mixer.music.play(fade_ms=350)
            currentScreen = Screens.PLAY
            gameplay = ui.Game()
        elif (e.type == GO_TO_MAINMENU.type):
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load(MAINMENU_BGM)
            pygame.mixer.music.play(fade_ms=350)
            instructionScreen = ui.Instruction()
            mainMenu = ui.MainMenu()
            currentScreen = Screens.MAIN_MENU
        elif (e.type == PAUSE.type):
            if (ctypes.windll.user32.MessageBoxW(0, "Do you want to continue playing?\nClick 'Yes' to resume.\nClick 'No' to exit.", "Game paused", MB_YESNO | ICON_INFO) == 7):
                instructionScreen = ui.Instruction()
                gameplay = ui.Game()
                mainMenu = ui.MainMenu()
                currentScreen = Screens.MAIN_MENU

    pygame.display.flip()
    clock.tick(120)