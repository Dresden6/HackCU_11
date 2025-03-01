import pygame
import random

class Map():
    
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # make a 2D array at start of program that includes all map tile types
        room_types = [0, 1, 2, 3, 4, 5] # types of roms to be filled into the grid, -1 is the start tile, 6 is the end tile
        generated_rooms = random.choices(room_types, k = 23)
        room_grid = [
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
                    if room_grid[i][j] != -1 and room_grid[i][j] != 6:
                        room_grid[i][j] = generated_rooms[index]
                        index += 1
        # every time you enter a room, render that tile type
        
        
    def changeRoom(SCREEN_WIDTH, SCREEN_HEIGHT, rooms, Tcell, room_grid, direction): # rooms is 2D array of tile types
        # determine which direction the player has moved, and update position in overworld
        #TODO: update overworld values to match
        if (direction == "north"):
            pass
        elif (direction == "south"):
            pass
        elif (direction == "east"):
            pass
        elif (direction == "west"):
            pass
        
        room_surface = pygame.Surface(SCREEN_WIDTH, SCREEN_HEIGHT)
        room_surface.fill((139, 0, 0)) # maroon
        
        # rendering of obstacles and/or spawning of enemies goes here
        
        

        
        
    
    