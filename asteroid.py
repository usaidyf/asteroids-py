from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
   def __init__(self, x, y, radius):
      super().__init__(x, y, radius)

   def draw(self, screen):
      pygame.draw.circle(screen, "green", self.position, self.radius, 2)

   def update(self, dt):
      self.position += self.velocity * dt

   def split(self):
      self.kill()
      if self.radius < ASTEROID_MIN_RADIUS:
         return 2
      
      separation_angle = random.uniform(20, 50)

      rot1 = self.velocity.rotate(separation_angle)
      ast1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
      ast1.velocity = rot1 * 1.2
      
      rot2 = self.velocity.rotate(-separation_angle)
      ast2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
      ast2.velocity = rot2 * 1.2
      
      return 1