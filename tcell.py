import pygame

class TCell(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)

        # TODO: Update to actual t-cell image
        self.image = pygame.image.load("./assets/tcell/tcell.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))

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
    
    def hasMovedRooms(self, SCREEN_WIDTH, SCREEN_HEIGHT): # returns boolean
        # check if player has moved out of bounds
        if self.x < 0:
            return True
        elif self.x > SCREEN_WIDTH:
            return True
        elif self.y < 0:
            return True
        elif self.y > SCREEN_HEIGHT:
            return True
        return False
    
    def findRoomMovementDirection():
        #TODO: similar to hasMovedRooms, find the direction the sprite is moving (north, south, east, west), and return as string
        pass