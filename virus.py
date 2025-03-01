import pygame
from random import randint

class Virus(pygame.sprite.Sprite):
    # creates the virus
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.width = width
        self.height = height

        self.image = pygame.image.load("./assets/virus/virus_idle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        
        self.rect = self.image.get_rect()
        self.speed = 5
        self.hit_countdown = 0
    
    # trying to make the virus flash when it is hit
    def update(self):      
        self._move()

    # makes the virus move randomly back and forth across the screen
    def _move(self):
        newpos = self.rect.move((self.speed, 0))
        # if not self.rect.contains(newpos):
        #     self.speed = -self.speed
        #     newpos = self.rect.move((self.speed, 0))
        #     self.image = pygame.transform.flip(self.image, True, False)
        self.rect = newpos
    
    def getLocation(self):
        return (self.rect.x, self.rect.y)

