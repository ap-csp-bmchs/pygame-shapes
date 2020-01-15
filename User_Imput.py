import pygame


shape = input("Pick a shape, Circle, Triangle, or Square:   ")
pygame.init()
display_width = 900
display_height = 700
screen = pygame.display.set_mode((display_width, display_height))
blue = (0, 0, 200)
purple = (64, 0, 120)
baby_blue = (3, 0, 205)
white = (255, 255, 255)
    

def Circle():
    screen.fill(white)
    pygame.draw.circle(screen, purple, (400, 400), 100)
    pygame.display.flip()

def Square():
   screen.fill(white)
   pygame.draw.rect(screen, baby_blue, (200, 200, 200, 200))
   pygame.display.flip()

def Triangle():
    screen.fill(white)
    pygame.draw.polygon(screen, blue, ((500, 300), (600, 400), (100, 700)))
    pygame.display.flip()

game_over = False
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if shape == 'Circle':
        Circle()

    if shape == 'Square':
        Square()

    if shape == 'Triangle':
        Triangle()
    else:
        print ("That's not an option stupid. Try again!")
        break
    

pygame.quit()
