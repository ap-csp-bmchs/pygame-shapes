import pygame
from pygame.locals import *
shape = input("Pick a shape between circle, square, and triangle ")
pygame.init()

display_width = 800
display_height = 600

surface = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Shapes')
white = (255, 255, 255)
black = (0, 0, 0)


def square():
    pygame.draw.rect(surface, white, (200, 200, 200, 200))
    pygame.display.flip()

def circle():
    pygame.draw.circle(surface, white, (200, 200), 200)
    pygame.display.flip()

def triangle():
    pygame.draw.polygon(surface, white, ((268, 0), (173, 57), (109, 256)))
    pygame.display.flip()

game_over = False
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    if shape == 'square':
        square()
    if shape == 'circle':
        circle()
    if shape == 'triangle':
        triangle()

pygame.quit()
    
        

    
