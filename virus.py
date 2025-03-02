import pygame
from random import randint

class Virus(pygame.sprite.Sprite):
    # creates the virus
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.maxspeed = 3
        
        self.width = width
        self.height = height
        
        self.radius = width / 4

        self.attacking = False
        
        self.x = x
        self.y = y
        
        self.attack_img = pygame.image.load("./assets/virus/virus_attack.png").convert_alpha()
        self.idle_img = pygame.image.load("./assets/virus/virus_idle.png").convert_alpha()

        self.image = self.idle_img
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        
        self.rect = self.image.get_rect()
        self.xspeed = randint(-self.maxspeed, self.maxspeed) # TODO Randomize location & have a min speed
        self.yspeed = randint(-self.maxspeed, self.maxspeed)
        self.hit_countdown = 0
    
    # trying to make the virus flash when it is hit
    def update(self):      
        self._move()

        self.hit_countdown += 1

        if (self.hit_countdown >= 100 ):
            self.hit_countdown = 0
            if (self.attacking):
                self.idle()
            else:
                self.attack()

    # makes the virus move randomly back and forth across the screen
    def _move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        # if not self.rect.contains(newpos):
        #     self.speed = -self.speed
        #     newpos = self.rect.move((self.speed, 0))
        #     self.image = pygame.transform.flip(self.image, True, False)
    
    
    def attack(self):
        self.image = self.attack_img
        self.attacking = True
    
    def idle(self):
        self.image = self.idle_img
        self.attacking = False
    
    def getLocation(self):
        return (self.x, self.y)

