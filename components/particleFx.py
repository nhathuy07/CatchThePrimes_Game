import time
from math import sin, cos, radians
from components import defaults
import pygame
from random import random
from typing import List
class Particle:
    def __init__(self, x: float, y:float, vel: float, size: float, shape: defaults.Graphics.DEFAULT_PARTICLE) -> None:
        self.x = x
        self.y = y
        self.angle = random() * 360
        self.vel = vel
        self.image = shape.copy().convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (size, size))
        self.alpha = 255
    def update(self, x: float, y: float, alpha_change_rate: float = 0.5):
        if (self.alpha > 0):
            self.alpha -= defaults.DEFAULT_ALPHA_CHANGE_RATE * alpha_change_rate
            self.image.set_alpha(self.alpha)
            self.y += (sin(radians(self.angle)) * self.vel / 60)
            self.x += (cos(radians(self.angle)) * self.vel / 60)
    def render(self, display: pygame.Surface):
        display.blit(self.image, (self.x, self.y))

class ParticleFx:
    def __init__(self, x: float, y: float, vel: float, size: float = 30, interval: float = 0.12, particle_shape = defaults.Graphics.DEFAULT_PARTICLE) -> None:
        self.shape = particle_shape
        self.x = x
        self.y = y
        self.vel = vel
        self.size = size
        self.interval = interval
        self.last_spawn = time.time()
        self.particles: List[Particle] = []
    def update(self, mode: defaults.ParticleModes = defaults.ParticleModes.NORM):
        if (mode == defaults.ParticleModes.NORM):
            if (time.time() - self.last_spawn >= self.interval):
                self.particles.append(Particle(self.x, self.y, self.vel, self.size, self.shape))
                self.last_spawn = time.time()

        for p in self.particles:
            if (p.alpha <= 0):
                self.particles.remove(p)
            else:
                p.update(self.x, self.y)
    def render(self, display: pygame.Surface):
        for p in self.particles:
            p.render(display)

    def burst(self, particle_cnt = 0):
        for i in range(particle_cnt):
            self.particles.append(Particle(self.x, self.y, self.vel, self.size, self.shape))