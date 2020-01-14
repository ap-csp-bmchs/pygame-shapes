import pygame
shape = input("pick a shape between circle, triangle, and square")
pygame.init()

display_width = 800
display_height = 600
surface = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Shapes')
white = (255, 255, 255)
black = (0, 0, 0)

def square():
    pygame.draw.rect(surface, white, (20,20,20,20))
    pygame.display.flip()

def circle():
    pygame.draw.circle(surface, white, (10, 10), 69)
    pygame.display.flip()

def triangle():
    pygame.draw.polygon(surface, white, ((10, 10),(15, 10),(12.5, 15)))
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







