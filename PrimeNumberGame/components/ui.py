import pygame
import time
from pathlib import Path

from components import defaults
from components import particleFx
from typing import List
from random import randint
from components import ball
from prime_sieve.list import PrimeListSieve
from math import floor
import stopwatch
import ctypes
# Common UI functions
class BaseUI:
    def __init__(self) -> None:
        pass
    def calculate_accel(self, vel: float, start_pos: float, end_pos: float = 0) -> float:
        return (-pow(vel, 2) / 2 / (end_pos - start_pos))


class MainMenu(BaseUI):
    def __init__(self):

        self.particle_fx = particleFx.ParticleFx(415, 315, 170)
                
        self.BACKGROUND_PATH = Path("assets/Clouds 2")
        self.FOREGROUND_PATH = Path("assets/Title")

        self.BG = pygame.image.load(self.BACKGROUND_PATH / "1 (1).png").convert_alpha()
        self.CLOUD_BACK = pygame.image.load(self.BACKGROUND_PATH / "2 (1).png").convert_alpha()
        self.CLOUD_MID = pygame.image.load(self.BACKGROUND_PATH / "3 (1).png").convert_alpha()
        self.CLOUD_FRONT = pygame.image.load(self.BACKGROUND_PATH / "4 (1).png").convert_alpha()

        self.TITLE = pygame.image.load(self.FOREGROUND_PATH / "Group 11.png").convert_alpha()
        self.PLAY_BTN = pygame.image.load(self.FOREGROUND_PATH / "Group 12.png").convert_alpha()
        
        self.play_btn_rect = self.PLAY_BTN.get_rect()
        self.play_btn_rect.topleft = (326.87, 258.13)

        self.cloud_back_pos = [0.0, -194]
        self.cloud_mid_pos = [0.0, 271]
        self.cloud_front_pos = [0.0, 419]
        self.ball23_pos = [210.45, 37.24]
        self.ball7_pos = [500, 159.63]
        self.ball0_pos = [362.69, 261.1]

        self.cloud_back_vel = defaults.DEFAULT_MAINMENU_ELEM_VEL
        self.cloud_mid_vel = -defaults.DEFAULT_MAINMENU_ELEM_VEL * 1.4
        self.cloud_front_vel = -defaults.DEFAULT_MAINMENU_ELEM_VEL * 2.3

        self.cloud_back_acc = self.calculate_accel(self.cloud_back_vel, self.cloud_back_pos[1])
        self.cloud_mid_acc = self.calculate_accel(self.cloud_mid_vel, self.cloud_mid_pos[1])
        self.cloud_front_acc = self.calculate_accel(self.cloud_front_vel, self.cloud_front_pos[1])

        self.title_alpha = 0

        if Path("hi_score.txt").exists():
            f = open("hi_score.txt", "r")
            self.hi_score = defaults.DEFAULT_FONT_SMALL.render(f"HI: {f.read()}", True, (168, 155, 202))
            self.hi_score_rect = self.hi_score.get_rect()
            self.hi_score_rect.center = (860 / 2, 141 + self.hi_score_rect.height / 2)
            f.close()

    def update(self, delta_time: float):
        self.title_alpha = min(self.title_alpha + defaults.DEFAULT_ALPHA_CHANGE_RATE, 255)

        self.TITLE.set_alpha(self.title_alpha)
        self.PLAY_BTN.set_alpha(self.title_alpha)

        self.cloud_back_pos[1] += self.cloud_back_vel / 60
        self.cloud_mid_pos[1] += self.cloud_mid_vel / 60
        self.cloud_front_pos[1] += self.cloud_front_vel / 60

        self.cloud_back_vel += (self.cloud_back_acc / 60)
        self.cloud_mid_vel += (self.cloud_mid_acc / 60)
        self.cloud_front_vel += (self.cloud_front_acc / 60)

        if (self.cloud_back_vel <= 0):
            self.cloud_back_pos[1] = 0
            self.cloud_back_acc = 0
            self.cloud_back_vel = 0
        if (self.cloud_front_vel >= 0):
            self.cloud_front_pos[1] = 0
            self.cloud_front_acc = 0
            self.cloud_back_vel = 0
        if (self.cloud_mid_vel >= 0):
            self.cloud_mid_pos[1] = 0
            self.cloud_mid_acc = 0
            self.cloud_back_vel = 0

        for e in pygame.event.get():
            if (e.type == pygame.MOUSEBUTTONDOWN and self.play_btn_rect.collidepoint(pygame.mouse.get_pos())):
                pygame.event.post(defaults.GO_TO_INSTRUCTION)
                
        self.particle_fx.update()


    def render(self, display: pygame.Surface):
        display.blit(self.BG, (0, 0))
        display.blit(self.CLOUD_BACK, self.cloud_back_pos)
        display.blit(self.CLOUD_MID, self.cloud_mid_pos)
        display.blit(self.CLOUD_FRONT, self.cloud_front_pos)
        display.blit(self.TITLE, (210.45, 16.77))
        self.particle_fx.render(display)
        display.blit(self.PLAY_BTN, self.play_btn_rect.topleft)
        if Path("hi_score.txt").exists():
            display.blit(self.hi_score, self.hi_score_rect.topleft)

class Instruction(BaseUI):

    def __init__(self) -> None:
        self.BACKGROUND_PATH = Path("assets/Clouds 2")
        self.BG = pygame.image.load(self.BACKGROUND_PATH / "1 (1).png").convert_alpha()
        self.CLOUD_BACK = pygame.image.load(self.BACKGROUND_PATH / "2 (1).png").convert_alpha()
        self.CLOUD_MID = pygame.image.load(self.BACKGROUND_PATH / "3 (1).png").convert_alpha()
        self.PLAY_BTN = pygame.image.load(Path("assets/clickPrompt.png")).convert_alpha()
        self.PLAY_BTN_HOVER = pygame.image.load(Path("assets/clickPrompt_hover.png")).convert_alpha()

        self.FOREGROUND = pygame.image.load(Path("assets/instruction_foreground.png")).convert_alpha()
        
        self.MAIN_MENU_GRAPHICS = pygame.image.load(Path("assets/MainMenuGraphic.png")).convert_alpha()

        self.play_btn_rect = self.PLAY_BTN.get_rect()
        self.play_btn_rect.topleft = (249, 403.51)

        self.background_alpha = 0
        self.foreground_alpha = 0
        self.foreground_pos = [(860 - 852) / 2, 470]
        self.foreground_vel = -defaults.DEFAULT_MAINMENU_ELEM_VEL * 4
        self.foreground_acc = self.calculate_accel(self.foreground_vel, self.foreground_pos[1])
    def update(self):
        self.foreground_alpha = min(self.foreground_alpha + 2, 255)
        self.background_alpha = min(self.background_alpha + defaults.DEFAULT_ALPHA_CHANGE_RATE * 1.2, 255)
        self.FOREGROUND.set_alpha(self.background_alpha)
        self.CLOUD_BACK.set_alpha(self.background_alpha)
        self.CLOUD_MID.set_alpha(self.background_alpha)
        self.BG.set_alpha(self.background_alpha)
        
        self.foreground_pos[1] += self.foreground_vel / 60
        self.foreground_vel += self.foreground_acc / 60

        if (self.foreground_vel >= 0):
            self.foreground_vel = 0
            self.foreground_acc = 0

        for e in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if (e.type == pygame.MOUSEBUTTONDOWN):
                pygame.event.post(defaults.PLAY)
    def render(self, display: pygame.Surface):
        display.blit(self.MAIN_MENU_GRAPHICS, (0, 0))
        display.blit(self.BG, (0, 0))
        display.blit(self.CLOUD_BACK, (0, 0))
        display.blit(self.CLOUD_MID, (0, 0))
        display.blit(self.FOREGROUND, self.foreground_pos)
        if (self.play_btn_rect.collidepoint(pygame.mouse.get_pos())):
            display.blit(self.PLAY_BTN_HOVER, self.play_btn_rect.topleft)
        else:
            display.blit(self.PLAY_BTN, self.play_btn_rect.topleft)

class Game(BaseUI):
    def __init__(self) -> None:
        self.sieve = PrimeListSieve()
        self.hud = HUD()

        self.BACKGROUND_PATH = Path("assets/Clouds 2")
        self.BG = pygame.image.load(self.BACKGROUND_PATH / "1 (1).png").convert_alpha()
        self.CLOUD_BACK = pygame.image.load(self.BACKGROUND_PATH / "2 (1).png").convert_alpha()
        self.CLOUD_MID = pygame.image.load(self.BACKGROUND_PATH / "3 (1).png").convert_alpha()
        self.STAR_OVERLAY = pygame.image.load("assets/star_overlay (Custom).png").convert_alpha()
        
        self.PAD_SPRITE = pygame.image.load(Path("assets/Pad.png")).convert_alpha()
        self.PAD_SILHOUETTE = pygame.image.load(Path("assets/Pad_silhouette.png")).convert_alpha()

        self.pad_rect = self.PAD_SPRITE.get_rect()
        self.pad_rect.center = [368, 425.31]
        self.overlay_alpha = 0
        self.overlay_dir = 0
        self.last_pad_x_pos = self.pad_rect.centerx
        self.target_pad_rotation = 0
        self.current_pad_rotation = 0
        
        self.particles: List[particleFx.Particle] = []
        self.last_particle_spawn = time.time()
        self.last_ball_spawn = stopwatch.Stopwatch(2)
        self.balls: List[ball.Ball] = []
        
        self.spawn_interval = 1.2
        self.spawn_interval_change = 0.15
        self.spawn_interval_change_thresh = 2500
        self.curr_mult = 0

        self.silhouette_alpha = 255

        self.score = 0
        self.hit_count = 0
        self.miss_count = 0
        self.ball_speed = 2

    def update(self) -> None:

        self.silhouette_alpha -= 1
        if (self.silhouette_alpha >= 0):
            self.PAD_SILHOUETTE.set_alpha(self.silhouette_alpha)
            self.hud.stopwatch.stop()

        self.pad_rect.centerx = pygame.mouse.get_pos()[0]

        if self.overlay_alpha < 0:
            self.overlay_dir = 0
        elif self.overlay_alpha > 275:
            self.overlay_dir = 1
        
        if self.overlay_dir == 1:
            self.overlay_alpha -= defaults.DEFAULT_ALPHA_CHANGE_RATE * 0.2
        else:
            self.overlay_alpha += defaults.DEFAULT_ALPHA_CHANGE_RATE * 0.2
        
        if (self.pad_rect.centerx - self.last_pad_x_pos > 0):
            self.target_pad_rotation = -6
            self.spawn_particles(1.6, self.pad_rect.center)
        elif (self.pad_rect.centerx - self.last_pad_x_pos < 0):
            self.target_pad_rotation = 6
            self.spawn_particles(1.6, self.pad_rect.center)
        else:
            self.target_pad_rotation = 0
        
        if (self.target_pad_rotation > self.current_pad_rotation):
            self.current_pad_rotation += 0.5
            
        elif (self.target_pad_rotation < self.current_pad_rotation):
            self.current_pad_rotation -= 0.5

        self.last_pad_x_pos = self.pad_rect.centerx

        self.STAR_OVERLAY.set_alpha(self.overlay_alpha)
        self.update_particles(self.pad_rect.center)
        if (self.silhouette_alpha <= 0):
            self.spawn_ball(self.spawn_interval)
            self.last_ball_spawn.start()
            self.hud.stopwatch.start()
        self.check_ball_collision()
        self.hud.update()
        
        if pygame.event.peek(pygame.KEYDOWN) and pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.event.post(defaults.PAUSE)
            self.hud.stopwatch.stop()
            self.last_ball_spawn.stop()

        if self.hud.time <= 0:
            EndScreen(self.score, self.hit_count, self.miss_count).show()

    def render(self, display: pygame.Surface):
        display.blit(self.BG, (0, 0))
        display.blit(self.STAR_OVERLAY, (43, 9))
        display.blit(self.CLOUD_BACK, (0, 0))
        display.blit(self.CLOUD_MID, (0, 0))
        self.hud.render(display)
        self.render_particles(display)
        
        display.blit(pygame.transform.rotozoom(self.PAD_SPRITE, self.current_pad_rotation, 1), self.pad_rect.topleft)
        if (self.silhouette_alpha > 0):
            display.blit(pygame.transform.rotozoom(self.PAD_SILHOUETTE, self.current_pad_rotation, 1), (self.pad_rect.left - 7, self.pad_rect.top - 7))

        for i in self.balls:
            i.render(display)

    def spawn_particles(self, interval, position):
        if (time.time() - self.last_particle_spawn > interval):
            self.particles.append(particleFx.Particle(position[0], position[1], 0, 25, defaults.Graphics.DEFAULT_PARTICLE))
    
    def update_particles(self, position):
        for i in self.particles:
            i.update(position[0], position[1], alpha_change_rate=0.9)
            if i.alpha <= 0:
                self.particles.remove(i)
    def render_particles(self, display):
        for i in self.particles:
            i.render(display)
    
    def spawn_ball(self, interval: float):
        if (self.last_ball_spawn.duration >= interval):
            random_x = randint(30, 860 - 30)
            self.balls.append(ball.Ball(random_x, vel_mult=self.ball_speed))
            self.last_ball_spawn.restart()
    def check_ball_collision(self):
        for i in self.balls:
            i.update()
            if (i.rect.colliderect(self.pad_rect)):
                if (self.sieve.is_prime(i.value)):
                    self.score += i.value
                    self.hit_count += i.value
                    self.hud.add_score(i.value, self.pad_rect.center)
                    # self.hud.speed_up()
                    if (self.check_thresh()):
                        self.spawn_interval -= self.spawn_interval_change
                        self.ball_speed += 0.15
                        self.hud.speed_up()
                        self.spawn_interval_change_thresh *= 2
                else:
                    self.score -= i.value
                    self.miss_count += i.value
                    self.hud.deduct_score(i.value)
                self.balls.remove(i)
    
    def check_thresh(self):
        b = (self.score > 0 and floor(self.score / self.spawn_interval_change_thresh) > self.curr_mult)
        self.curr_mult = max(floor(self.score / self.spawn_interval_change_thresh), self.curr_mult)
        return b

class HUD:
    def __init__(self) -> None:
        self.score = 0
        self.last_fx_call = 0
        self.time = 90
        self.stopwatch = stopwatch.Stopwatch(1)
        self.stopwatch.reset()
        self.SCORE_DEDUCTION_FX = pygame.image.load(Path("assets/scoredeductionfx.png")).convert_alpha()
        self.PAUSE_ICON = pygame.image.load(Path("assets/pause.png")).convert_alpha()
        self.SPEED_UP = pygame.image.load(Path("assets/speed_up.png")).convert_alpha()
        self.sd_fx_alpha = 0

        self.particleSystem = particleFx.ParticleFx(0, 0, defaults.DEFAULT_MAINMENU_ELEM_VEL * 2, 25, particle_shape=defaults.Graphics.STAR_PARTICLE)

        self.score_disp = defaults.DEFAULT_FONT_2DIG.render(f'{self.score:09}', True, (255, 255, 255))
        self.score_rect = self.score_disp.get_rect()
        self.score_rect.center = (860 / 2, 30)

        self.last_su_fx_call = 0
        self.time_disp_color = defaults.TIMER_COLOR
    def deduct_score(self, points: int):
        self.score -= points
        self.sd_fx_alpha = 255
        self.last_fx_call = time.time()
    def update(self):
        self.particleSystem.update(mode=defaults.ParticleModes.BURST)
        if self.sd_fx_alpha > 0:
            self.sd_fx_alpha -= defaults.DEFAULT_ALPHA_CHANGE_RATE * 2.2
        else:
            self.sd_fx_alpha = 0

        if (time.time() - self.last_su_fx_call <= 1):
            if (0 <= time.time() - self.last_su_fx_call < 0.2
            or 0.4 <= time.time() - self.last_su_fx_call < 0.6
            or 0.8 <= time.time() - self.last_su_fx_call < 1
            ):
                self.SPEED_UP.set_alpha(255)
            else:
                self.SPEED_UP.set_alpha(0)
        else:
            self.SPEED_UP.set_alpha(0)

        self.SCORE_DEDUCTION_FX.set_alpha(self.sd_fx_alpha)
        self.score_disp = defaults.DEFAULT_FONT_2DIG.render(f'{self.score:09}', True, (255, 255, 255))
        self.update_timer()

    def render(self, display: pygame.Surface):
        if (self.sd_fx_alpha > 0):
            display.blit(self.SCORE_DEDUCTION_FX, (0, 430))

        if (self.SPEED_UP.get_alpha() > 0):
            display.blit(self.SPEED_UP, (302, 75))
        self.particleSystem.render(display)
        display.blit(self.score_disp, self.score_rect.topleft)

        self.time_disp = pygame.draw.rect(display, self.time_disp_color, pygame.Rect(0, 0, 860 * (self.time / 90), 13), 0, 15)
    
    def add_score(self, points: int, particle_pos = tuple[int, int]):
        self.score += points
        self.particleSystem.x = particle_pos[0]
        self.particleSystem.y = particle_pos[1]
        self.particleSystem.burst(12)

    def speed_up(self):
        self.last_su_fx_call = time.time()
    
    def update_timer(self):
        self.time = 90 - self.stopwatch.duration
        if (self.time < 20):
            self.time_disp_color = defaults.TIMER_WARNING_COLOR


class EndScreen:
    def __init__(self, score: int, hit: int, miss: int) -> None:
        self.title = f"Final score:".center(50)
        self.score = str(score).center(50)
        self.s = score
        if not Path("hi_score.txt").exists():
            f = open("hi_score.txt", 'w')
            f.write(str(score))
            f.close()
        else:
            f = open("hi_score.txt", "r")
            if (int(f.read()) < self.s):
                self.title = f"HIGH SCORE!".center(50)
                f.close()
                f = open("hi_score.txt", "w")
                f.write(str(self.s))
                f.close()
        
    def show(self):
        if (ctypes.windll.user32.MessageBoxW(0, f"{self.title}\n{self.score}", "Time's Up", defaults.MB_OK) == 1):
            pygame.event.post(defaults.GO_TO_MAINMENU)