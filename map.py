import pygame
import random

class Map():
    
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
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
        
    def changeRoom(self, SCREEN_WIDTH, SCREEN_HEIGHT, rooms, Tcell, room_grid, direction): # rooms is 2D array of tile types
        
        # determine which direction the player has moved, and update position in overworld
        if (direction == "north"):
            self.overworldY += 1
        elif (direction == "south"):
            self.overworldY -= 1
        elif (direction == "east"):
            self.overworldX += 1
        elif (direction == "west"):
            self.overworldX -= 1
        
        room_surface = pygame.Surface(SCREEN_WIDTH, SCREEN_HEIGHT)
        
        # here, check content of room in room_grid, then render in background as specified in the room type
        
        room_surface.fill((139, 0, 0)) # maroon
        
        # rendering of obstacles and/or spawning of enemies goes here
        
        

        
        
    
    