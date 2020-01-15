import pygame
from pygame.locals import *
pygame.init()

display_width = 900
display_height = 800
SURFACE = pygame.display.set_mode((display_width, display_height))



pygame.display.set_caption('Shapes')
clock = pygame.time.Clock()

LAVENDER = (230, 230, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SURFACE.fill(LAVENDER)
pygame.display.update()
shape = input("Pick a shape for me to draw: a circle, rectangle, or triangle ")



    
def tri():
    pygame.draw.polygon(SURFACE, WHITE, ((200, 100), (150, 300), (250, 280)))
    
def rect():
    pygame.draw.rect(SURFACE, BLACK, (500, 350, 200, 250))
    
def circ():
    pygame.draw.circle(SURFACE, WHITE, [100, 100], 80, 1)

#game loop


while True:


#set up quit when user clicks the 'x'
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    if shape == "triangle":
        tri()
        
    if shape == "rectangle":
        rect()

    if shape == "circle":
        circ()
                

    
    pygame.display.update()   
                
   
       
            
    
pygame.quit()

















