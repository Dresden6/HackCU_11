import math
import pygame
from virus import Virus

class Virus2(Virus):
    # creates the virus
    def __init__(self, width, height, x, y):

        super().__init__(width, height, x, y)
        
        self.image = pygame.image.load("./assets/virus/virus_2_idle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        
        
        self.rotation = 0
        
    def _move(self):
        
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed

        
    def attack(self):
        self.image = pygame.image.load("./assets/virus/virus_2_attack.png").convert_alpha()
        self.attacking = True
    
    def idle(self):
        self.image = pygame.image.load("./assets/virus/virus_2_idle.png").convert_alpha()
        self.attacking = False
        
        
        
    def changeVelocityTowardsPlayer(self, playerCoords):
        
        rotation = math.atan2(playerCoords[1] - self.rect.y, playerCoords[0] - self.rect.x)
        
        error = self.rotation - rotation
        
        
        # Clamp error
        if error > 0.01:
            error = 0.01
        elif error < -0.01:
            error = -0.01
            
        self.rotation -= error # Adjust rotation        
        
        # Calc speeds
        self.xspeed = self.maxspeed * math.cos(self.rotation)
        self.yspeed = self.maxspeed * math.sin(self.rotation)
        
        print(self.xspeed, self.yspeed)
        

    
    