# Example file showing a basic pygame "game loop"
import pygame

from tcell import TCell
from virus import Virus
from virus2 import Virus2
from map import Map

# pygame setup
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080 # Everything should be done in reference to these screen dimensions

CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT = 854, 480 # These dimensions are only for calculating resizing

screen = pygame.display.set_mode((CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

# Calculate scale based on screen size. Should take in a touple of (width, height)
def scaleToScreenSize(size, eventSize):
    width_ratio = eventSize[0] / SCREEN_WIDTH
    height_ratio = eventSize[1] / SCREEN_HEIGHT
    return (int(size[0] * width_ratio), int(size[1] * height_ratio))
    
# Scale coordinates based on screen size. Base size is 1920x1080. Should take in a touple of (x, y)
def scaleCoordinates(coords, eventSize):
    width_ratio = eventSize[0] / SCREEN_WIDTH
    height_ratio = eventSize[1] / SCREEN_HEIGHT
    return (int(coords[0] * width_ratio), int(coords[1] * height_ratio))

pygame.display.set_caption('Going Viral')
pygame.display.set_icon(pygame.image.load("./assets/virus/virus_idle.png"))

font = pygame.font.Font(None, 36)

intro = True

time_loop = True

while (intro):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro = False
            time_loop = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
        intro = False
    
    screen.fill((0, 0, 0))
    text = font.render("Going Viral", True, "#FFFFFF")
    screen.blit(text, (100, 100))

    text = font.render("We're under attack! You are a white blood cell, ", True, "#FFFFFF")
    screen.blit(text, (100, 180))

    text = font.render("and your job is to protect us from viruses.", True, "#FFFFFF")
    screen.blit(text, (100, 220))

    text = font.render("(WASD to start)", True, "#FFFFFF")
    screen.blit(text, (100, 260))
    pygame.display.flip()



# Create main background image
backgroundImg = pygame.image.load("./assets/environment/background.png").convert()

collected = {}

while time_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            time_loop = False
        if event.type == pygame.VIDEORESIZE:
                CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT = event.size
                
                # Keep aspect ratio
                if CURR_SCREEN_WIDTH == pygame.display.Info().current_w:
                    CURR_SCREEN_WIDTH = 16/9 * CURR_SCREEN_HEIGHT
                elif CURR_SCREEN_HEIGHT == pygame.display.Info().current_h:
                    CURR_SCREEN_HEIGHT = 9/16 * CURR_SCREEN_WIDTH
                else:
                    CURR_SCREEN_HEIGHT = 9/16 * CURR_SCREEN_WIDTH
                
                if CURR_SCREEN_WIDTH < 854 or CURR_SCREEN_HEIGHT < 480:
                    CURR_SCREEN_WIDTH = 854
                    CURR_SCREEN_HEIGHT = 480
                
                screen = pygame.display.set_mode((CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT), pygame.RESIZABLE) # Resize window
                backgroundImg = pygame.transform.scale(backgroundImg, (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)) # Resize background image

    player_cell = TCell(140, 140, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    map = Map(SCREEN_WIDTH, SCREEN_HEIGHT)
    viruses = map.spawnEnemies()    
    
    sprites = pygame.sprite.RenderPlain([player_cell] + viruses)


    # Scale everything correctly:
    for sprite in sprites:
                    sprite.image = pygame.transform.scale(sprite.image, scaleToScreenSize((sprite.width, sprite.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)))
                    sprite.rect.width, sprite.rect.height = scaleToScreenSize((sprite.width, sprite.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT))

    eligibleToMoveRooms = False # default value for flag having to do with map crossing
    running = True
    
    bodyCount = 0
    NUM_I_FRAMES = 25
        

    while running:
        backgroundImg = pygame.transform.scale(backgroundImg, (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)) # Resize background image
        
        
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                time_loop = False
            if event.type == pygame.VIDEORESIZE:
                CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT = event.size
                
                # Keep aspect ratio
                if CURR_SCREEN_WIDTH == pygame.display.Info().current_w:
                    CURR_SCREEN_WIDTH = 16/9 * CURR_SCREEN_HEIGHT
                elif CURR_SCREEN_HEIGHT == pygame.display.Info().current_h:
                    CURR_SCREEN_HEIGHT = 9/16 * CURR_SCREEN_WIDTH
                else:
                    CURR_SCREEN_HEIGHT = 9/16 * CURR_SCREEN_WIDTH
                
                if CURR_SCREEN_WIDTH < 854 or CURR_SCREEN_HEIGHT < 480:
                    CURR_SCREEN_WIDTH = 854
                    CURR_SCREEN_HEIGHT = 480
                
                screen = pygame.display.set_mode((CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT), pygame.RESIZABLE) # Resize window
                backgroundImg = pygame.transform.scale(backgroundImg, (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)) # Resize background image
                
                # for sprite in sprites:
                #     sprite.image = pygame.transform.scale(sprite.image, scaleToScreenSize((sprite.width, sprite.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)))
                #     sprite.rect.width, sprite.rect.height = scaleToScreenSize((sprite.width, sprite.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT))
                #     pass
            
        
            
        # Player Movement  

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_cell.moveLeft()
        if keys[pygame.K_d]:
            player_cell.moveRight()
        if keys[pygame.K_w]:
            player_cell.moveUp()
        if keys[pygame.K_s]:
            player_cell.moveDown()
            
            
            
        # check if player has moved rooms
        
        if (len(sprites) == 1):
            eligibleToMoveRooms = True
        
        if (player_cell.hasMovedRooms(SCREEN_WIDTH, SCREEN_HEIGHT) and eligibleToMoveRooms):
            eligibleToMoveRooms = False
            direction = player_cell.findRoomMovementDirection(SCREEN_WIDTH, SCREEN_HEIGHT)
            if (not map.movingOffMap(direction)):
                screen.fill((0,0,0))
                pygame.display.flip()
                pygame.time.delay(250)
                #respwanws viruses when changing rooms
                viruses = map.spawnEnemies()
                
                
                sprites = pygame.sprite.RenderPlain([player_cell] + viruses)


                # Scale everything correctly:
                for sprite in sprites:
                                sprite.image = pygame.transform.scale(sprite.image, scaleToScreenSize((sprite.width, sprite.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)))
                                sprite.rect.width, sprite.rect.height = scaleToScreenSize((sprite.width, sprite.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT))
                backgroundImg = pygame.transform.scale(backgroundImg, (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)) # Resize background image
                
                map.changeRoom(player_cell, direction)
                
                # Move player to correct place
                if direction == "north":
                    player_cell.y = SCREEN_HEIGHT - 64
                elif direction == "south":
                    player_cell.y = 0 + 64
                elif direction == "west":
                    player_cell.x = SCREEN_WIDTH - 64
                elif direction == "east":
                    player_cell.x = 0 + 64
            
        # if (player_cell.backToMiddle(SCREEN_WIDTH, SCREEN_HEIGHT)):


        for virus in viruses:
            if (virus.x > SCREEN_WIDTH or virus.x < 0):
                virus.xspeed = -virus.xspeed
            if (virus.y > SCREEN_HEIGHT or virus.y < 0):
                virus.yspeed = -virus.yspeed
                
            if (pygame.sprite.collide_rect(virus, player_cell)):
                 if (player_cell.x <= virus.x + 60 and player_cell.x >= virus.x - 60
                        and player_cell.y <= virus.y + 60 and player_cell.y >= virus.y - 60):
                    if (virus.attacking):
                        running = False
                    else:
                        virus.kill()
                        sprites.remove(virus)
                    # bodyCount == len(viruses) - 1
            if (isinstance(virus, Virus2)):
                virus.changeVelocityTowardsPlayer((player_cell.x, player_cell.y))

         
    
                    
        
        if (len(sprites) == 1):
            # map.clearCurrentRoom()
            pass

        
        # Resize coordinates for everything 
        for sprite in sprites:
            sprite.image = pygame.transform.scale(sprite.image, scaleToScreenSize((sprite.width, sprite.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)))
            sprite.rect.width, sprite.rect.height = scaleToScreenSize((sprite.width, sprite.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT))
            sprite.rect.center = scaleCoordinates((sprite.x, sprite.y), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)) # Probably a better way to do this

        sprites.update()
        
        
        for door in map.doors:
            door.image = pygame.transform.scale(door.image, scaleToScreenSize((door.width, door.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)))
            door.rect.width, door.rect.height = scaleToScreenSize((door.width, door.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT))
            door.rect.center = scaleCoordinates((door.x, door.y), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)) # Probably a better way to do this

        for lock in map.locks:
            lock.image = pygame.transform.scale(lock.image, scaleToScreenSize((lock.width, lock.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)))
            lock.rect.width, lock.rect.height = scaleToScreenSize((lock.width, lock.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT))
            lock.rect.center = scaleCoordinates((lock.x, lock.y), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)) # Probably a better way to do this

        # Draw Everything

        screen.blit(backgroundImg, (0, 0)) # Draw background
        map.doors.draw(screen) # Draw doors
        if(not eligibleToMoveRooms): map.locks.draw(screen) # Draw locks
        sprites.draw(screen) # Draw sprites    

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
        
    print("Your kill count for this round was: " + str(bodyCount))
    


pygame.quit()