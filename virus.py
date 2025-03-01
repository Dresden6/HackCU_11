import pygame
from random import randint

class Virus(pygame.sprite.Sprite):
    # creates the virus
    def __init__(self, width, height, x, y):
        
        self.width = width
        self.height = height

        # TODO: Update to actual t-cell image
        self.image = pygame.image.load("./assets/tcell/virus_idle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        

        pygame.sprite.Sprite.__init__(self)
        # screen = pygame.display.get_surface()
        self.area = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.move = 10
        self.hit_countdown = 0
    
    # trying to make the virus flash when it is hit
    def update(self):      
        if self.hit_countdown:
            if not hasattr(self):
                self.original_image = self.image

            if self.hit_countdown % 2:
                self.image = None 
            else:
              self.image = self.original_image

            self.hit_countdown = max(0, self.hit_countdown - 1)

    # makes the virus move randomly back and forth across the screen
    def _move(self):
        newpos = self.rect.move((self.move, 0))
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left or self.rect.right > self.area.right:
                self.move = -self.move
                newpos = self.rect.move((self.move, 0))
                self.image = pygame.transform.flip(self.image, True, False)
        self.rect = newpos
    
