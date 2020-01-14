import pygame
shape = input("pick a shape btw circle,trangle, and square ")
pygame.init()

display_width = 1000
display_height = 800
surface = pygame.display.set_mode((500, 400))
pygame.display.set_caption('shapes')
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)

surface.fill(green)
gmae_over = False
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if shape == 'square':
        pygame.draw.rect(surface, black, (150, 150, 150, 150))
        pygame.display.flip()
    if shape == 'triangle':
        pygame.draw.polygon(surface, black, ((268, 0), (173, 47), (109, 256)))
        pygame.display.flip()
    if shape == 'circle':
        pygame.draw.circle(surface, black, (300, 300), 100)
    #else:
        print("Not an option, try again.")
        
pygame.quit()
