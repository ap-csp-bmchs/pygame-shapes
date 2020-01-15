import pygame
from pygame.locals import *
pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((500,400))
gameDisplay.fill(black)
pygame.display.set_caption('shapes')
pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green


def circle():
    pygame.draw.circle(gameDisplay, green, (200, 150), 100, 10)
    

def square():
    pygame.draw.rect(gameDisplay, green, pygame.Rect(50, 50, 100, 100), 10)

def polygon():
    pygame.draw.polygon(gameDisplay, green, ((146,0),(291,106), (236,277)))
    




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    choice = input("Do you want to draw a circle, triangle, square, ?: ") 
    if choice == "circle":
        pygame.time.wait(50)
        gameDisplay.fill(black)
        circle()
        
    elif choice == "square":
        pygame.time.wait(50)
        gameDisplay.fill(black)
        square()
        
    elif choice == "triangle":
        pygame.time.wait(50)
        gameDisplay.fill(black)
        polygon()
        
    else:
        print("please choose an available option!")
        
   
    
    pygame.display.update()

