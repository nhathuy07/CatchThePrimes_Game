from components.defaults import DEFAULT_MAINMENU_ELEM_VEL, DEFAULT_FONT_2DIG, DEFAULT_FONT_3DIG, F_COLORS
from random import randint, choice
import pygame
from pathlib import Path
from prime_sieve import list

sieve = list.PrimeListSieve()
prime = sieve.primes_in_range(2, 600)

class Ball:
    def __init__(self, x: float, y = 0, vel_mult: int = 2) -> None:
        self.x = x
        self.y = y

        self.opts = randint(1, 10)
        if (1 <= self.opts <= 6):
            self.value = choice(prime)
        else:
            self.value = randint(2, 600)
        self.type = randint(1, 3)
        self.image_path = f"assets/Balls/b{self.type}.png"
        self.font = None
        if (len(str(self.value)) < 3):
            self.font = DEFAULT_FONT_2DIG
        else:
            self.font = DEFAULT_FONT_3DIG

        self.label = self.font.render(str(self.value), True, F_COLORS[self.type - 1])
        self.label_rect = self.label.get_rect()

        self.sprite = pygame.image.load(Path(self.image_path)).convert_alpha()
        self.vel_mult = vel_mult
        self.vel = DEFAULT_MAINMENU_ELEM_VEL * self.vel_mult
        self.acc = 9.8
        self.rect = self.sprite.get_rect()
        self.rect.center = (self.x, self.y)
        self.label_rect.center = self.rect.center
    def update(self):
        self.y += self.vel / 120
        self.vel += self.acc / 120
        self.rect.centery = self.y
        self.label_rect.center = self.rect.center
    def render(self, display: pygame.Surface):
        display.blit(self.sprite, self.rect.topleft)
        display.blit(self.label, self.label_rect.topleft)
    def change_speed(self, delta: float):
        self.vel_mult += delta