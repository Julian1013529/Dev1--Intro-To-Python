import pygame
import sys
import random
import time

pygame.init()

width = 500
length = 500
screen = pygame.display.set_mode((width, height))

class screen():

    def __init__(self):
        self.width = 500
        self.height = 500


    def create_screen(self):
        return screen.display.set_mode((self.width, self.height))

myscreen = screen()
myscreen.create_screen()

myscreen2 = screen()
myscreen2.create_screen()


class sprite():

    def __init__(self, posx, posy):
        self.width = 10
        self.height = 10
        self.color = (0, 0, 255)
        self.posx = posx
        self.posy = posy
        self.dist = 5

    def create_sprite(self, screen):
        return pygame.draw.rect(screen, self.color, (self.posx, self.posy, self.height, self.height, self.width))

    def movement(self, direction):

        if direction == "UP":
            self.posy -= self.dist
        elif direction == "DOWN":
            self.posy += self.dist
        elif direction == "LEFT":
            self.posx -= self.dist
        elif direction == "RIGHT":
            self.posx += self.dist


raul = sprite(50, 50)
kevin = sprite(50, 80)
isabella = sprite(30, 60)

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                raul.movement("UP")
            if event.key == pygame.K_UP:
                isabella.movement("UP")
            if event.key == pygame.K_ESCAPE:
                kevin.movement("UP")
