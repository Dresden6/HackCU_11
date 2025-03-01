import pygame

class TCell(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.width = width
        self.height = height

        # TODO: Update to actual t-cell image
        self.image = pygame.image.load("./assets/tcell/tcell.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.x = x
        self.y = y

        self.speed = 2

        self.rect = self.image.get_rect()
    

    def update(self):
        pass

    def moveLeft(self):
        self.rect.x -= self.speed

    def moveRight(self):
        self.rect.x += self.speed

    def moveUp(self):
        self.rect.y += self.speed

    def moveDown(self):
        self.rect.y -= self.speed

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y