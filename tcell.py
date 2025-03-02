import pygame

class TCell(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.width = width
        self.height = height

        self.radius = width / 4

        self.image = pygame.image.load("./assets/tcell/tcell.png").convert_alpha()

        # x and y are the position in a 1920x1080 screen
        self.x = x
        self.y = y

        self.speed = 6

        self.rect = self.image.get_rect()
        # self.rect.center = (x, y)

    def update(self):
        pass

    def moveLeft(self):
        if(self.x > 0): 
            self.x -= self.speed

    def moveRight(self):
        if(self.x < 1920): 
            self.x += self.speed

    def moveUp(self):
        if(self.y > 0): 
            self.y -= self.speed

    def moveDown(self):
        if(self.y < 1080): 
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
        if self.x < 1:
            return True
        elif self.x > SCREEN_WIDTH - 1:
            return True
        elif self.y < 1:
            return True
        elif self.y > SCREEN_HEIGHT - 1:
            return True
        return False
    
    
    def findRoomMovementDirection(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.x < 2:
            return "west"
        elif self.x > SCREEN_WIDTH - 2:
            return "east"
        elif self.y < 2:
            return "north"
        elif self.y > SCREEN_HEIGHT - 2:
            return "south"
        return None