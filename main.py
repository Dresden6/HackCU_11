# Example file showing a basic pygame "game loop"
import pygame

from tcell import TCell
from virus import Virus
from map import Map

# pygame setup
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True


pygame.display.set_caption('Biology Platformer')


# create a surface object, image is drawn on it.
imp = pygame.image.load("./assets/testBackground.jpg").convert()

info = pygame.display.Info()
player_cell = TCell(20, 20, info.current_h/2, info.current_w/2)
sprites = pygame.sprite.RenderPlain((player_cell))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_cell.moveLeft()
    if keys[pygame.K_RIGHT]:
        player_cell.moveRight()
    if keys[pygame.K_DOWN]:
        player_cell.moveUp()
    if keys[pygame.K_UP]:
        player_cell.moveDown()

    sprites.update()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    sprites.draw(screen)

    # screen.blit(imp, (0, 0))
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()