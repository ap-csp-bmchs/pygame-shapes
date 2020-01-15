import pygame
#from pygame.locals import *
shape = input("Pick a shape, Circle, Triangle, Square:")
pygame.init()

display_width = 1000
display_height = 800
DISPLAYSURF = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Shapes')
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

DISPLAYSURF.fill(white)

    
    
game_over = False
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if shape == 'Triangle':
        pygame.draw.polygon(DISPLAYSURF, blue, ((268, 0), (173, 47), (109, 256)))
        pygame.display.flip()

    if shape == 'Circle':
        pygame.draw.circle(DISPLAYSURF, blue, (300, 300), 100)
        pygame.display.flip()

    if shape == 'Square':
        pygame.draw.rect(DISPLAYSURF, blue, (150, 150, 150, 150))
        pygame.display.flip()


    else:
        print ("Not an option, try again.")
        break
    
pygame.quit()

