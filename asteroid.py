import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self,dt):
        self.position += self.velocity * dt 
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20,50)
        vec1 = self.velocity.rotate(rand_angle)
        vec2 = self.velocity.rotate(-rand_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x,self.position.y,new_rad)
        ast2 = Asteroid(self.position.x,self.position.y,new_rad)
        ast1.velocity = vec1 * 1.2
        ast2.velocity = vec2 * 1.2