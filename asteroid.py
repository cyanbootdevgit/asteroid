import pygame

import random

from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen,):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position = self.velocity * dt + self.position

    def split(self):
        self.kill()
        #wouldn't that already be killed?
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else:
            log_event("asteroid_split")
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            rnd = random.uniform(20, 50)
            v1 = self.velocity.rotate(rnd)
            v2 = self.velocity.rotate(-rnd)
            
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = v1 * 1.2
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = v2 * 1.2
        return [a1, a2]


