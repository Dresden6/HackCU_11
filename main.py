# Example file showing a basic pygame "game loop"
import pygame

from tcell import TCell
from virus import Virus
from map import Map

# pygame setup
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 854, 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
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


# Create main background image
backgroundImg = pygame.image.load("./assets/environment/background.png").convert()

info = pygame.display.Info()
player_cell = TCell(128, 128, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
basic_virus = Virus(128, 128, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 40)
map = Map(SCREEN_WIDTH, SCREEN_HEIGHT)
sprites = pygame.sprite.RenderPlain([player_cell] + viruses)


# Scale everything correctly:
for sprite in sprites:
                sprite.image = pygame.transform.scale(sprite.image, scaleToScreenSize((sprite.width, sprite.height), (SCREEN_WIDTH, SCREEN_HEIGHT)))
backgroundImg = pygame.transform.scale(backgroundImg, (SCREEN_WIDTH, SCREEN_HEIGHT)) # Resize background image


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            SCREEN_WIDTH, SCREEN_HEIGHT = event.size
            
            # Keep aspect ratio
            if SCREEN_WIDTH == pygame.display.Info().current_w:
                SCREEN_WIDTH = 16/9 * SCREEN_HEIGHT
            elif SCREEN_HEIGHT == pygame.display.Info().current_h:
                SCREEN_HEIGHT = 9/16 * SCREEN_WIDTH
            else:
                SCREEN_HEIGHT = 9/16 * SCREEN_WIDTH
            
            if SCREEN_WIDTH < 854 or SCREEN_HEIGHT < 480:
                SCREEN_WIDTH = 854
                SCREEN_HEIGHT = 480
            
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE) # Resize window
            backgroundImg = pygame.transform.scale(backgroundImg, (SCREEN_WIDTH, SCREEN_HEIGHT)) # Resize background image
            
            for sprite in sprites:
                sprite.image = pygame.transform.scale(sprite.image, scaleToScreenSize((sprite.width, sprite.height), (SCREEN_WIDTH, SCREEN_HEIGHT)))
                pass
          
          
          
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
    if (player_cell.hasMovedRooms(SCREEN_WIDTH, SCREEN_HEIGHT)):
        direction = player_cell.findRoomMovementDirection()
        map.changeRoom(direction)

    for virus in viruses:
        virus_x = virus.getLocation()[0]
        if (virus_x > SCREEN_WIDTH or virus_x < 0):
            virus.speed = -virus.speed

    for virus in viruses:
        virus_x = virus.getLocation()[0]
        if (virus_x > SCREEN_WIDTH or virus_x < 0):
            virus.speed = -virus.speed

    sprites.update()




    # Draw Everything

    screen.blit(backgroundImg, (0, 0)) # Draw background
    sprites.draw(screen) # Draw sprites    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()