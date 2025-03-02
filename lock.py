import pygame

class Lock(pygame.sprite.Sprite):
    # creates the virus
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
            
        self.width = width
        self.height = height
            
        self.x = x
        self.y = y
    

        self.image = pygame.image.load("./assets/environment/lock.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        