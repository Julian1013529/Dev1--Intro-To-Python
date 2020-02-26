import pygame
import sys

pygame.init()

width = 500
height = 500



screen = pygame.display.set_mode((500, 500))

### CORDINATES FOR MY SHAPE ###
posx = 250
posy = 250

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                posx -= 10
            if event.key == pygame.K_d:
                posx += 10
            if event.key == pygame.K_w:
                posy -= 10
            if event.key == pygame.K_s:
                posy += 10

    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_LEFT] and posx > 100:
        posx -= 10
    if keypress[pygame.K_RIGHT] and posx < 400:
        posx += 10
    if keypress[pygame.K_UP] and posy > 100:
        posy -= 10
    if keypress[pygame.K_DOWN] and posy < 400:
        posy += 10

    screen.fill((255, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (posx, posy), 100)
    pygame.display.update()
