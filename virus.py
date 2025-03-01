import pygame

class Virus(pygame.sprite.Sprite):
    def __init__(self):
        
        self.image = pygame.image.load("./assets/virus/virus_idle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        
        pass