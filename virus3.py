from random import choice 
import pygame
from virus import Virus

class Virus3(Virus):
    # creates the virus
    def __init__(self, width, height, x, y):

        super().__init__(width, height, x, y)

        self.attack_img = pygame.image.load("./assets/virus/virus_3_attack.png").convert_alpha()
        self.idle_img = pygame.image.load("./assets/virus/virus_3_idle.png").convert_alpha()
        
        self.image = self.idle_img
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        
        
        self.rotation = 0
        
        self.speeds = [-8, -7, -6, -5, 5, 6, 7, 8]
        self.xspeed = choice(self.speeds) 
        self.yspeed = choice(self.speeds)
        
        
    
    def update(self):      
        self._move()

        self.hit_countdown += 1

        if (self.hit_countdown >= 50 ):
            self.hit_countdown = 0
            if (self.attacking):
                self.idle()
            else:
                self.attack()
                
                
    
    def _move(self):
        self.x += self.xspeed
        self.y += self.yspeed

        
    def attack(self):
        self.image = self.attack_img
        self.attacking = True
    
    def idle(self):
        self.image = self.idle_img
        self.attacking = False
        
