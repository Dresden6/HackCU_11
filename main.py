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
    


pygame.display.set_caption('Biology Platformer')


# Create main background image
imp = pygame.image.load("./assets/testBackground.jpg").convert()


# Initialize the player cell
info = pygame.display.Info()
player_cell = TCell(128, 128, info.current_h/2, info.current_w/2)
basic_virus = Virus(128, 128, info.current_h/2, info.current_w/2)
map = Map(SCREEN_WIDTH, SCREEN_HEIGHT)

sprites = pygame.sprite.RenderPlain((player_cell))


# Scale everything correctly:
for sprite in sprites:
                sprite.image = pygame.transform.scale(sprite.image, scaleToScreenSize((sprite.width, sprite.height), (SCREEN_WIDTH, SCREEN_HEIGHT)))


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
            
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE) # Resize window
            imp = pygame.transform.scale(imp, (SCREEN_WIDTH, SCREEN_HEIGHT)) # Resize background image
            
            for sprite in sprites:
                sprite.image = pygame.transform.scale(sprite.image, scaleToScreenSize((sprite.width, sprite.height), (SCREEN_WIDTH, SCREEN_HEIGHT)))
                pass
            

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_cell.moveLeft()
    if keys[pygame.K_RIGHT]:
        player_cell.moveRight()
    if keys[pygame.K_DOWN]:
        player_cell.moveUp()
    if keys[pygame.K_UP]:
        player_cell.moveDown()
        
    # check if player has moved rooms
    # if (player_cell.hasMovedRooms(SCREEN_WIDTH, SCREEN_HEIGHT)):
    #     direction = player_cell.findRoomMovementDirection()
    #     map.changeRoom(direction)

    sprites.update()

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(imp, (0, 0))

    sprites.draw(screen)

    # screen.blit(imp, (0, 0))
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()