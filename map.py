import pygame
import random

class Map():
    
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # make a 2D array at start of program that includes all map tile types
        
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
        
        # here, check content of room in room_grid, then render in objects as specified in the room type
        
        # rendering of obstacles and/or spawning of enemies goes here
        
        

        
        
    
    