import pygame
import random

class Map():
    
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # store constants for width and height inside class for easy access
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT
        
        rows, columns = 5,5
        room_grid = [["" for _ in range(columns)] for _ in range(rows)]
        # populating the grid with the generated rooms
        for row in range(rows):
            for column in range(columns):
                if row == 0:
                    if column == 0:
                        room_grid[row][column] = "start"
                    elif column == columns - 1:
                        room_grid[row][column] = "top_right_corner"
                    else:
                        room_grid[row][column] = "top_edge"
                elif row == rows - 1:
                    if column == columns - 1:
                        room_grid[row][column] = "finish"
                    elif column == 0:
                        room_grid[row][column] = "bottom_left_corner"
                    else:
                        room_grid[row][column] = "bottom_edge"
                elif column == 0:
                    room_grid[row][column] = "left_edge"
                elif column == columns - 1:
                    room_grid[row][column] = "right_edge"
                else:
                    room_grid[row][column] = "middle"
        
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