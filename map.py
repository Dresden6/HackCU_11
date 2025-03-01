import pygame
import random

class Map():
    
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # store constants for width and height inside class for easy access
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT
        
        # make a 2D array at start of program that includes all map tile types
        self.room_types = [0, 1, 2, 3, 4, 5] # types of roms to be filled into the grid, -1 is the start tile, 6 is the end tile
        generated_rooms = random.choices(self.room_types, k = 23)
        self.room_grid = [
            [-1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,6]
        ]
        # populating the grid with the generated rooms
        index = 0
        for i in range(5):
            for j in range(5):
                    if self.room_grid[i][j] != -1 and self.room_grid[i][j] != 6:
                        self.room_grid[i][j] = generated_rooms[index]
                        index += 1
        # every time you enter a room, render that tile type
        
        # set player overworld position to position of start tile
        self.overworldX = 0
        self.overworldY = 0
        
    def getOverworldX(self):
        return self.overworldX
        
    def getOverworldY(self):
        return self.overworldY
        
    def changeRoom(self, Tcell, roomTypes, direction): # rooms is 2D array of tile types
        
        # determine which direction the player has moved, and update position in overworld
        # also change the position of the player based on what direction they're coming in from
        if (direction == "north"):
            self.overworldY += 1
            Tcell.setY(0) # move player's y position to top
        elif (direction == "south"):
            self.overworldY -= 1
            Tcell.setY(self.SCREEN_HEIGHT) # move player's y position to bottom
        elif (direction == "east"):
            self.overworldX += 1
            Tcell.setX(self.SCREEN_WIDTH) # move player's x position to right
        elif (direction == "west"):
            self.overworldX -= 1
            Tcell.setX(0) # move player's x position to left
        
        # spawn in new room's background, obstacles, and enemies
        self.spawnRoom(self)
        self.spawnObstacles(self)
        self.spawnEnemies(self)

    def spawnRoom(self):
        room_surface = pygame.Surface(self.SCREEN_WIDTH, self.SCREEN_HEIGHT) # should i be passing this in instead?
        
        # TODO: look at room type at self.overworldX and self.overworldY, then render the proper room background as specified in self.room_types
        
        room_surface.fill((139, 0, 0)) # placeholder
        
    def spawnObstacles(self):
        # TODO: look at room type at self.overworldX and self.overworldY, then render the proper obstacles as specified in self.room_types, making sure they don't overlap with the background sprite
        pass
        
    def spawnEnemies(self):
        # TODO: look at room type at self.overworldX and self.overworldY, then render the proper obstacles as specified in self.room_types, making sure they don't overlap with the background sprite OR the obstacles
        pass