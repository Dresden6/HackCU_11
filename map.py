import pygame
import random

class Tile():
    def __init__(self):
        self.doors = [True, True, True, True] # True means it's bloked
        self.enemies = []
        self.obstacles = []
        self.name = "default"
    

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
                        new_tile = Tile()
                        new_tile.name = "start"
                        new_tile.doors[1] = False
                        new_tile.doors[3] = False
                        room_grid[row][column] = new_tile
                    elif column == columns - 1:
                        new_tile = Tile()
                        new_tile.name = "top_right_corner"
                        new_tile.doors[2] = False
                        new_tile.doors[3] = False
                        room_grid[row][column] = new_tile
                    else:
                        new_tile = Tile()
                        new_tile.name = "top_edge"
                        new_tile.doors[1] = False
                        new_tile.doors[2] = False
                        new_tile.doors[3] = False
                        room_grid[row][column] = new_tile
                elif row == rows - 1:
                    if column == columns - 1:
                        new_tile = Tile()
                        new_tile.name = "finish"
                        new_tile.doors[0] = False
                        new_tile.doors[3] = False
                        room_grid[row][column] = new_tile
                    elif column == 0:
                        new_tile = Tile()
                        new_tile.name = "bottom_left_corner"
                        new_tile.doors[0] = False
                        new_tile.doors[1] = False
                        room_grid[row][column] = new_tile
                    else:
                        new_tile = Tile()
                        new_tile.name = "bottom_edge"
                        new_tile.doors[0] = False
                        new_tile.doors[1] = False
                        new_tile.doors[3] = False
                        room_grid[row][column] = new_tile
                elif column == 0:
                    new_tile = Tile()
                    new_tile.name = "left_edge"
                    new_tile.doors[0] = False
                    new_tile.doors[1] = False
                    new_tile.doors[2] = False
                    room_grid[row][column] = new_tile
                elif column == columns - 1:
                    new_tile = Tile()
                    new_tile.name = "right_edge"
                    new_tile.doors[0] = False
                    new_tile.doors[2] = False
                    new_tile.doors[3] = False
                    room_grid[row][column] = new_tile
                else:
                    new_tile = Tile()
                    room_types = [1,2,3,4,5]
                    new_tile.name = str(random.choice(room_types))
                    new_tile.doors[0] = False
                    new_tile.doors[1] = False
                    new_tile.doors[2] = False
                    new_tile.doors[3] = False
                    room_grid[row][column] = new_tile
        
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