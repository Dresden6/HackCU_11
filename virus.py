import pygame
from random import randint

class Virus(pygame.sprite.Sprite):
    # creates the virus
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.width = width
        self.height = height
        
        
        self.attacking = False
        
        self.x = x
        self.y = y

        self.image = pygame.image.load("./assets/virus/virus_idle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        
        self.rect = self.image.get_rect()
        self.xspeed = randint(-3, 3)
        self.yspeed = randint(-3, 3)
        self.hit_countdown = 0
    
    # trying to make the virus flash when it is hit
    def update(self):      
        self._move()

    # makes the virus move randomly back and forth across the screen
    def _move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        # if not self.rect.contains(newpos):
        #     self.speed = -self.speed
        #     newpos = self.rect.move((self.speed, 0))
        #     self.image = pygame.transform.flip(self.image, True, False)
    
    
    def attack(self):
        self.image = pygame.image.load("./assets/virus/virus_attack.png").convert_alpha()
        self.attacking = True
    
    def idle(self):
        self.image = pygame.image.load("./assets/virus/virus_idle.png").convert_alpha()
        self.attacking = False
    
    def getLocation(self):
        return (self.rect.x, self.rect.y)

