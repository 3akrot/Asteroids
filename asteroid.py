import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame

from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        
    def draw(self,screen: pygame.Surface):

        pygame.draw.circle(screen, "white",self.position,self.radius,LINE_WIDTH)
    
    def update(self,dt):
        
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        velcocity1 = self.velocity.rotate(angle)
        velcocity2 = self.velocity.rotate(-angle)
        new_raduis = self.radius - ASTEROID_MIN_RADIUS
        one = Asteroid(self.position.x,self.position.y,new_raduis)
        one.velocity = velcocity1
        two = Asteroid(self.position.x,self.position.y,new_raduis)
        two.velocity = velcocity2
        

        
