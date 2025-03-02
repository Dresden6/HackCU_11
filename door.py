import pygame

class Door(pygame.sprite.Sprite):
    # creates the virus
    def __init__(self, width, height, x, y, rotation, locked):
        pygame.sprite.Sprite.__init__(self)
            
        if(rotation):
            self.width = height * 6
            self.height = width * 6
        else:
            self.width = width * 6
            self.height = height * 6
            
        self.x = x
        self.y = y
    

        self.door_image = pygame.image.load("./assets/environment/door.png").convert_alpha()
        self.black_door_image = pygame.image.load("./assets/environment/black_door.png").convert_alpha()
        self.door_image_vert = pygame.image.load("./assets/environment/door_vert.png").convert_alpha()
        self.black_door_image_vert = pygame.image.load("./assets/environment/black_door_vert.png").convert_alpha()
        
        self.update(locked, rotation)
        
        self.rect = self.image.get_rect()
        
    
    def update(self, locked, rotation):
        self.locked = locked
        
        print(rotation)
        
        if locked: 
            if rotation:
                self.image = self.black_door_image_vert
            else:
                self.image = self.black_door_image
        else:
            if rotation:
                self.image = self.door_image_vert
            else:
                self.image = self.door_image
        
        
        

    

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)

