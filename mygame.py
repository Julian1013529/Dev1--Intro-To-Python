import pygame
import sys
### INITIATING THE LIBRARY ###
pygame.init()


### SCREEN DIMENSIONS ###
width = 800
height = 500

### CREATING THE SCREEN ###
screen = pygame.display.set_mode((width, height))


### INITIATE THE SCREEN ###
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill((255, 0, 255))  ### SCREEN IS RED
    pygame.display.flip()
