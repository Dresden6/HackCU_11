import pygame

class Map():
    
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # make a 2D array at start of program that includes all map tile types
        
        
        # every time you enter a room, render that tile type
        pass
        
        
    def renderRoom(SCREEN_WIDTH, SCREEN_HEIGHT, rooms, Tcell): # rooms is 2D array of tile types
        room_surface = pygame.Surface(SCREEN_WIDTH, SCREEN_HEIGHT)
        room_surface.fill((139, 0, 0)) # maroon
        
        # rendering of obstacles and/or spawning of enemies goes here
        
        player_x = Tcell.get_x()
        player_y = Tcell.get_y()
        
        player_size = Tcell.get_size()

        # Change rooms when leaving the current one
        if player_x < 0:
            current_room = (current_room - 1) % len(rooms)
            player_x = SCREEN_WIDTH - player_size
        elif player_x > SCREEN_WIDTH:
            current_room = (current_room + 1) % len(rooms)
            player_x = 0
        elif player_y < 0:
            current_room = (current_room - 1) % len(rooms)
            player_y = SCREEN_HEIGHT - player_size
        elif player_y > SCREEN_HEIGHT:
            current_room = (current_room + 1) % len(rooms)
            player_y = 0
        
    
    