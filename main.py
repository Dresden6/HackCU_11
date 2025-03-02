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
    width_ratio = eventSize[0] / 1920
    height_ratio = eventSize[1] / 1080
    return (int(size[0] * width_ratio), int(size[1] * height_ratio))
    
# Scale coordinates based on screen size. Base size is 1920x1080. Should take in a touple of (x, y)
def scaleCoordinates(coords, eventSize):
    width_ratio = eventSize[0] / 1920
    height_ratio = eventSize[1] / 1080
    return (int(coords[0] * width_ratio), int(coords[1] * height_ratio))

pygame.display.set_caption('Biology Platformer')

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
    text = font.render("going viral", True, "#FFFFFF")
    screen.blit(text, (100, 100))

    text = font.render("we're under attack! you are a white blood cell, ", True, "#FFFFFF")
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

    player_cell = TCell(128, 128, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    map = Map(SCREEN_WIDTH, SCREEN_HEIGHT)
    viruses = map.spawnEnemies()
    viruses2 = [Virus2(128, 128, SCREEN_WIDTH/6, SCREEN_HEIGHT/6 + 40)]
    
    
    sprites = pygame.sprite.RenderPlain([player_cell] + viruses + viruses2)


    # Scale everything correctly:
    for sprite in sprites:
                    sprite.image = pygame.transform.scale(sprite.image, scaleToScreenSize((sprite.width, sprite.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)))
                    sprite.rect.width, sprite.rect.height = scaleToScreenSize((sprite.width, sprite.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT))
    backgroundImg = pygame.transform.scale(backgroundImg, (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)) # Resize background image

    eligibleToMoveRooms = True # default value for flag having to do with map crossing
    running = True
    
    # bodyCount = 0

    while running:
        
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
        
        if (player_cell.hasMovedRooms(SCREEN_WIDTH, SCREEN_HEIGHT) and eligibleToMoveRooms):
            eligibleToMoveRooms = False
            direction = player_cell.findRoomMovementDirection(SCREEN_WIDTH, SCREEN_HEIGHT)
            if (not map.movingOffMap(direction)):
                map.changeRoom(player_cell, direction)
                # TODO: add a screen change here to indicate to the player they changed positions
                
            if direction == "up":
                player_cell.y = SCREEN_HEIGHT - player_cell.height
            elif direction == "down":
                player_cell.y = 0
            elif direction == "left":
                player_cell.x = SCREEN_WIDTH - player_cell.width
            elif direction == "right":
                player_cell.x = 0
            
        # if (player_cell.backToMiddle(SCREEN_WIDTH, SCREEN_HEIGHT)):
            eligibleToMoveRooms = True


        for virus in viruses:
            if (virus.x > SCREEN_WIDTH or virus.x < 0):
                virus.xspeed = -virus.xspeed
            if (virus.y > SCREEN_HEIGHT or virus.y < 0):
                virus.yspeed = -virus.yspeed

            if (pygame.sprite.collide_rect(virus, player_cell)):
                if (virus.attacking):
                    running = False
                elif (player_cell.x <= virus.x + 10 and player_cell.x >= virus.x - 10
                        and player_cell.y <= virus.y + 10 and player_cell.y >= virus.y - 10):
                    virus.kill()
                    # bodyCount == len(viruses) - 1
                    
        
        if (len(viruses) == 0):
            map.clearCurrentRoom()

        # for virus in viruses2:
        #     virus.changeVelocityTowardsPlayer((player_cell.x, player_cell.y))
        #     for virus in viruses:
        #         if (virus.x > SCREEN_WIDTH or virus.x < 0):
        #             virus.xspeed = -virus.xspeed
        #         if (virus.y > SCREEN_HEIGHT or virus.y < 0):
        #             virus.yspeed = -virus.yspeed

        # Resize coordinates for everything 
        for sprite in sprites:
            sprite.image = pygame.transform.scale(sprite.image, scaleToScreenSize((sprite.width, sprite.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)))
            sprite.rect.width, sprite.rect.height = scaleToScreenSize((sprite.width, sprite.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT))
            sprite.rect.center = scaleCoordinates((sprite.x, sprite.y), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)) # Probably a better way to do this

        sprites.update()
        
        # Resize coordinates for everything 
        for door in map.doors:
            door.image = pygame.transform.scale(door.image, scaleToScreenSize((door.width, door.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)))
            door.rect.width, door.rect.height = scaleToScreenSize((door.width, door.height), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT))
            door.rect.center = scaleCoordinates((door.x, door.y), (CURR_SCREEN_WIDTH, CURR_SCREEN_HEIGHT)) # Probably a better way to do this


        # Draw Everything

        screen.blit(backgroundImg, (0, 0)) # Draw background
        map.doors.draw(screen) # Draw doors
        sprites.draw(screen) # Draw sprites    

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
        
    # print("Your kill count for this round was: " + str(bodyCount))
    


pygame.quit()