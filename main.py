# Example file showing a basic pygame "game loop"
import pygame

from tcell import TCell
from virus import Virus
from map import Barrier

# pygame setup
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption('Biology Platformer')


# create a surface object, image is drawn on it.
imp = pygame.image.load("./assets/testBackground.jpg").convert()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")


    screen.blit(imp, (0, 0))
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()