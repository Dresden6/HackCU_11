import pygame
import random

class Map():
    
    # doors = pygame.sprite.RenderPlain([player_cell] + viruses)
    
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # store constants for width and height inside class for easy access
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT
        
        rows, columns = 5,5
        self.room_grid = [["" for _ in range(columns)] for _ in range(rows)]
        # populating the grid with the generated rooms
        for row in range(rows):
            for column in range(columns):
                if row == 0:
                    if column == 0:
                        self.room_grid[row][column] = "start"
                    elif column == columns - 1:
                        self.room_grid[row][column] = "top_right_corner"
                    else:
                        self.room_grid[row][column] = "top_edge"
                elif row == rows - 1:
                    if column == columns - 1:
                        self.room_grid[row][column] = "finish"
                    elif column == 0:
                        self.room_grid[row][column] = "bottom_left_corner"
                    else:
                        self.room_grid[row][column] = "bottom_edge"
                elif column == 0:
                    self.room_grid[row][column] = "left_edge"
                elif column == columns - 1:
                    self.room_grid[row][column] = "right_edge"
                else:
                    self.room_types = [1,2,3,4,5]
                    room_type = random.choice(self.room_types)
                    self.room_grid[row][column] = str(room_type)
        
        # set player overworld position to position of start tile
        self.overworldX = 0
        self.overworldY = 0
        
    def getOverworldX(self):
        return self.overworldX
        
    def getOverworldY(self):
        return self.overworldY
        
    def changeRoom(self, player_cell, direction): # rooms is 2D array of tile types
        
        # determine which direction the player has moved, and update position in overworld
        # also change the position of the player based on what direction they're coming in from
        #TODO: block the player from moving outside the bounds of the overworld
        if (direction == "north"):
            self.overworldY += 1
            player_cell.setY(0) # move player's y position to top
        elif (direction == "south"):
            self.overworldY -= 1
            player_cell.setY(self.SCREEN_HEIGHT) # move player's y position to bottom
        elif (direction == "east"):
            self.overworldX += 1
            player_cell.setX(self.SCREEN_WIDTH) # move player's x position to right
        elif (direction == "west"):
            self.overworldX -= 1
            player_cell.setX(0) # move player's x position to left
        
        # spawn in new room's background, obstacles, and enemies
        selectedTile = self.room_grid[self.overworldX][self.overworldY]
        
        self.despawnOldEntities(selectedTile)
        self.spawnRoom(selectedTile)
        self.spawnObstacles(selectedTile)
        self.spawnEnemies(selectedTile)
        
    # despawns old enemies, obstacles, etc
    def despawnOldEntities(self, selectedTile):
        pass

    def spawnRoom(self, selectedTile):
        print("new room")
        
        # true = door spawned in; false = door not spawned in
        # a door blocks movement to another room in a different direction
        
        for i in selectedTile.doors:
            if (selectedTile.doors[0]): # north
                pass
            elif (selectedTile.doors[1]): # east
                pass
            elif (selectedTile.doors[2]): # south
                pass
            elif (selectedTile.doors[3]): # west
                pass
        
        # TODO: look at room type at self.overworldX and self.overworldY, then render the proper room using door placements
        
    def spawnObstacles(self, selectedTile):
        # TODO: look at room type at self.overworldX and self.overworldY, then render the proper obstacles as specified in self.room_types, making sure they don't overlap with the background sprite
        pass
        
    def spawnEnemies(self, selectedTile):
        # TODO: look at room type at self.overworldX and self.overworldY, then render the proper obstacles as specified in self.room_types, making sure they don't overlap with the background sprite OR the obstacles
        pass