import pygame

class Door(pygame.sprite.Sprite):
    # creates the virus
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
            
        self.width = width
        self.height = height
    

        self.locked = False
        
        self.x = x
        self.y = y

        self.image = pygame.image.load("./assets/virus/virus_idle.png").convert_alpha()
        # self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        
    
    def update(self, locked, rotation):
        if locked: 
            self.image = pygame.image.load("./assets/environment/black_door.png").convert_alpha()
        else:
            self.image = pygame.image.load("./assets/environment/door.png").convert_alpha()
        
        self.locked = locked
        self.rotate(rotation)
    

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)

