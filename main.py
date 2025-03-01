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
def scaleToScreenSize(size):
    width_ratio = SCREEN_WIDTH / 1920
    height_ratio = SCREEN_HEIGHT / 1080
    return (int(size[0] * width_ratio), int(size[1] * height_ratio))
    


pygame.display.set_caption('Biology Platformer')


# Create main background image
imp = pygame.image.load("./assets/testBackground.jpg").convert()

info = pygame.display.Info()
player_cell = TCell(20, 20, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
basic_virus = Virus(128, 128, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 40)
map = Map(SCREEN_WIDTH, SCREEN_HEIGHT)
sprites = pygame.sprite.RenderPlain((player_cell))

# Scale everything correctly:
for sprite in sprites:
                sprite.image = pygame.transform.scale(sprite.image, scaleToScreenSize((sprite.width, sprite.height)))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            for sprite in sprites:
                sprite.image = pygame.transform.scale(sprite.image, scaleToScreenSize((sprite.width, sprite.height)))
            

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
        map.changeRoom(SCREEN_WIDTH, SCREEN_HEIGHT, direction)

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