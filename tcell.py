import pygame

class TCell(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.width = width
        self.height = height

        self.image = pygame.image.load("./assets/tcell/tcell.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # x and y are the position in a 1920x1080 screen
        self.x = x
        self.y = y

        self.speed = 4

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.center = (self.x, self.y)
        pass

    def moveLeft(self):
        self.x -= self.speed

    def moveRight(self):
        self.x += self.speed

    def moveUp(self):
        self.y -= self.speed

    def moveDown(self):
        self.y += self.speed

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, newX):
        self.x = newX
    
    def setY(self, newY):
        self.y = newY
    
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
    
    def findRoomMovementDirection(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.x < 0:
            return "west"
        elif self.x > SCREEN_WIDTH:
            return "east"
        elif self.y < 0:
            return "north"
        elif self.y > SCREEN_HEIGHT:
            return "south"
        return None