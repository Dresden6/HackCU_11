import pygame
import random
from door import Door
from virus import Virus
from virus2 import Virus2
from virus3 import Virus3
from lock import Lock

class Tile():
    def __init__(self):
        self.doors = [True, True, True, True] # True means it's blocked
        self.enemies = []
        self.obstacles = []
        self.name = "default"
    

class Map():
    
    doors = pygame.sprite.RenderPlain()
    locks = pygame.sprite.RenderPlain()
    
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # store constants for width and height inside class for easy access
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT
        
        self.MAP_ROWS, self.MAP_COLUMNS = 5,5
        self.room_grid = [["" for _ in range(self.MAP_COLUMNS)] for _ in range(self.MAP_ROWS)]
        # populating the grid with the generated rooms
        for row in range(self.MAP_ROWS):
            for column in range(self.MAP_COLUMNS):
                if row == 0:
                    if column == 0:
                        new_tile = Tile()
                        new_tile.name = "start"
                        new_tile.doors[1] = False
                        new_tile.doors[2] = False
                        self.room_grid[row][column] = new_tile
                    elif column == self.MAP_COLUMNS - 1:
                        new_tile = Tile()
                        new_tile.name = "top_right_corner"
                        new_tile.doors[2] = False
                        new_tile.doors[3] = False
                        self.room_grid[row][column] = new_tile
                    else:
                        new_tile = Tile()
                        new_tile.name = "top_edge"
                        new_tile.doors[1] = False
                        new_tile.doors[2] = False
                        new_tile.doors[3] = False
                        self.room_grid[row][column] = new_tile
                elif row == self.MAP_ROWS - 1:
                    if column == self.MAP_COLUMNS - 1:
                        new_tile = Tile()
                        new_tile.name = "finish"
                        new_tile.doors[0] = False
                        new_tile.doors[3] = False
                        self.room_grid[row][column] = new_tile
                    elif column == 0:
                        new_tile = Tile()
                        new_tile.name = "bottom_left_corner"
                        new_tile.doors[0] = False
                        new_tile.doors[1] = False
                        self.room_grid[row][column] = new_tile
                    else:
                        new_tile = Tile()
                        new_tile.name = "bottom_edge"
                        new_tile.doors[0] = False
                        new_tile.doors[1] = False
                        new_tile.doors[3] = False
                        self.room_grid[row][column] = new_tile
                elif column == 0:
                    new_tile = Tile()
                    new_tile.name = "left_edge"
                    new_tile.doors[0] = False
                    new_tile.doors[1] = False
                    new_tile.doors[2] = False
                    self.room_grid[row][column] = new_tile
                elif column == self.MAP_COLUMNS - 1:
                    new_tile = Tile()
                    new_tile.name = "right_edge"
                    new_tile.doors[0] = False
                    new_tile.doors[2] = False
                    new_tile.doors[3] = False
                    self.room_grid[row][column] = new_tile
                else:
                    new_tile = Tile()
                    room_types = [1,2,3,4,5]
                    new_tile.name = str(random.choice(room_types))
                    new_tile.doors[0] = False
                    new_tile.doors[1] = False
                    new_tile.doors[2] = False
                    new_tile.doors[3] = False
                    self.room_grid[row][column] = new_tile
        
        # set player overworld position to position of start tile
        self.overworldX = 0
        self.overworldY = 0
        
        self.spawnRoom(self.room_grid[self.overworldX][self.overworldY])
        
    def getOverworldX(self):
        return self.overworldX
        
    def getOverworldY(self):
        return self.overworldY
    
    
    def movingOffMap(self, direction):
        if ((direction == "north" and (self.overworldY <= 0))
            or (direction == "south" and (self.overworldY >= self.MAP_ROWS - 1))
            or (direction == "west" and (self.overworldX >= 0))
            or (direction == "east" and (self.overworldX >= self.MAP_COLUMNS - 1))):
            return True
        return False
        
    def changeRoom(self, player_cell, direction): # rooms is 2D array of tile types
        
        # determine which direction the player has moved, and update position in overworld
        # also change the position of the player based on what direction they're coming in from
        
        if (direction == "north"):
            self.overworldY -= 1
            player_cell.setY(0) # move player's y position to top
        elif (direction == "south"):
            self.overworldY += 1
            player_cell.setY(self.SCREEN_HEIGHT) # move player's y position to bottom
        elif (direction == "east"):
            self.overworldX += 1
            player_cell.setX(self.SCREEN_WIDTH) # move player's x position to right
        elif (direction == "west"):
            self.overworldX -= 1
            player_cell.setX(0) # move player's x position to left
        
        # spawn in new room's background, obstacles, and enemies
        # print("overworld x: " + (str)(self.overworldX))
        # print("overworld y: " + (str)(self.overworldY))
        selectedTile = self.room_grid[self.overworldY][self.overworldX]
        
        self.despawnOldEntities(selectedTile)
        self.spawnRoom(selectedTile)
        self.spawnObstacles(selectedTile)
        
    # despawns old enemies, obstacles, etc
    def despawnOldEntities(self, selectedTile):
        pass

    def spawnRoom(self, selectedTile):
        
        # true = door spawned in; false = door not spawned in
        # a door blocks movement to another room in a different direction
        
        
        self.doors = pygame.sprite.RenderPlain([
            Door(64, 16, self.SCREEN_WIDTH/2, 0, False, selectedTile.doors[0]),
            Door(64, 16, self.SCREEN_WIDTH, self.SCREEN_HEIGHT/2, True, selectedTile.doors[1]),
            Door(64, 16, self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT, False, selectedTile.doors[2]),
            Door(64, 16, 0, self.SCREEN_HEIGHT/2, True, selectedTile.doors[3])
        ])
        
        
        self.locks = pygame.sprite.RenderPlain()
        
        if(not selectedTile.doors[0]):
            Lock(64, 64, self.SCREEN_WIDTH/2, 40).add(self.locks)
        if(not selectedTile.doors[1]):
            Lock(64, 64, self.SCREEN_WIDTH - 30, self.SCREEN_HEIGHT/2).add(self.locks)
        if(not selectedTile.doors[2]):
            Lock(64, 64, self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT - 40).add(self.locks)
        if(not selectedTile.doors[3]):
            Lock(64, 64, 30, self.SCREEN_HEIGHT/2).add(self.locks)
            
        
        # --------------------------------------------------------------------------------------------------------
        # To be immortalized forever in the hall of shame:
        #
        # for i in selectedTile.doors:
        #     if (selectedTile.doors[0]): # north
        #         pass
        #     elif (selectedTile.doors[1]): # east
        #         pass
        #     elif (selectedTile.doors[2]): # south
        #         pass
        #     elif (selectedTile.doors[3]): # west
        #         pass
        #
        #
        #      I met a programmer from an antique land,
        #      Who said—“Eight vast and functionless lines of code
        #      Stand in map.py. . . . Near them, in the lines,
        #      Commented away, a shattered for loop lies, whose cases,
        #      And stupid logic, and pretense of functionality,
        #      Tell that its creator well those Redbulls drank
        #      Which yet survive, commented in these lifeless files,
        #      The team members that mocked them, and the members that laughed;
        #      And in the comment, these words appear:
        #      My name is Alex, Major of CS;
        #      Look on my Works, ye Mighty, and despair!
        #      Nothing beside remains. Round the decay
        #      Of that colossal Wreck, boundless and bare
        #      The lone and level functions stretch far away.”
        # --------------------------------------------------------------------------------------------------------
        
    def spawnObstacles(self, selectedTile):
        # TODO: look at room type at self.overworldX and self.overworldY, then render the proper obstacles as specified in self.room_types, making sure they don't overlap with the background sprite
        pass

    def getRandomCoords(self):
        CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT = 854, 480
        x = random.choice(list(range(CURR_SCREEN_WIDTH//8, 3*CURR_SCREEN_WIDTH//8)) + list(range(5*CURR_SCREEN_WIDTH//8, 7*CURR_SCREEN_WIDTH//8)))
        y = random.choice(list(range(CURR_SCREEN_HEIGHT//8, 3*CURR_SCREEN_HEIGHT//8)) + list(range(5*CURR_SCREEN_HEIGHT//8, 7*CURR_SCREEN_HEIGHT//8)))
        return (x, y)
        
    def spawnEnemies(self):
        
        difficulty = random.randint(3,7)
        result = []
        for i in range(difficulty):
            x, y = self.getRandomCoords()
            result.append(Virus(128, 128, x, y))
        
        x, y = self.getRandomCoords()
        result.append(Virus2(128, 128, x, y))

        x, y = self.getRandomCoords()
        result.append(Virus3(128, 128, x, y))
        
        if difficulty > 3:
            x, y = self.getRandomCoords()
            result.append(Virus2(128, 128, x, y))
        if difficulty > 4: 
            x, y = self.getRandomCoords()
            result.append(Virus3(128, 128, x, y))
        if difficulty > 5:
            x, y = self.getRandomCoords()
            result.append(Virus2(128, 128, x, y))
        if difficulty > 6:
            x, y = self.getRandomCoords()
            result.append(Virus2(128, 128, x, y))
        
        return result

        # TODO: look at room type at self.overworldX and self.overworldY, then render the proper obstacles as specified in self.room_types, making sure they don't overlap with the background sprite OR the obstacles
        pass