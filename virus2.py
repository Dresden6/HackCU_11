import math
import pygame
from virus import Virus

class Virus2(Virus):
    # creates the virus
    def __init__(self, width, height, x, y):

        super().__init__(width, height, x, y)

        self.attack_img = pygame.image.load("./assets/virus/virus_2_attack.png").convert_alpha()
        self.idle_img = pygame.image.load("./assets/virus/virus_2_idle.png").convert_alpha()
        
        self.image = self.idle_img
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        
        
        self.rotation = 0
        
        self.maxspeed = 5
        
    def _move(self):
        
        
        # Clamp speeds
        if self.xspeed > self.maxspeed:
            self.xspeed = self.maxspeed
        elif self.xspeed < -self.maxspeed:
            self.xspeed = -self.maxspeed

        if self.yspeed > self.maxspeed:
            self.yspeed = self.maxspeed
        elif self.yspeed < -self.maxspeed:
            self.yspeed = -self.maxspeed
        
        self.x += self.xspeed
        self.y += self.yspeed

        
    def attack(self):
        self.image = self.attack_img
        self.attacking = True
    
    def idle(self):
        self.image = self.idle_img
        self.attacking = False
        
        
        
    def changeVelocityTowardsPlayer(self, playerCoords):
        
        errx = playerCoords[0] - self.x
        erry = self.y - playerCoords[1]
        
        
        maxAcc = 0.1
        
        # Clamp error
        if errx > maxAcc:
            errx = maxAcc
        elif errx < -maxAcc:
            errx = -maxAcc
            
        if erry > maxAcc:
            erry = maxAcc
        elif erry < -maxAcc:
            erry = -maxAcc
            
            
        
        # Calc speeds
        self.xspeed += errx
        self.yspeed -= erry 
        
        
        
        # print(self.xspeed, self.yspeed)
        

    
    