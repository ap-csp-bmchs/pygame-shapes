import pygame
pygame.init()

#game area
win = arena = pygame.display.set_mode((800, 800))
win.fill((255, 255, 255))
pygame.display.update()
pygame.display.set_caption("Pick a shape")
clock = pygame.time.Clock()
circles = pygame.image.load('circled.png')
triangles = pygame.image.load('triangled.png')
squares = pygame.image.load('squared.png')
tbox = pygame.image.load('textbox.png')
tbox_st = True
user_str = ""
arial = pygame.font.SysFont('arial', 15)
arial2 = pygame.font.SysFont('arial', 30)
inst = arial.render("Enter a shape (circle, triangle, square): ", True, (0, 0, 0))
txt = arial2.render("test", True, (0, 0, 0))
txt_str = ""

#game loop
while True:

    # quit on x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #update positions
    win.fill((255, 255, 255))
    if tbox_st:
        win.blit(inst, (225,365))
        win.blit(tbox, (225,380))
        win.blit(txt, (225,380))
    pygame.display.update()

    #get key input for text input
    if tbox_st:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "q"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "w"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "e"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "r"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "t"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "y"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "u"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "i"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "o"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "p"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "a"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "s"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "d"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "f"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "g"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "h"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "j"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "k"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "l"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "z"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "x"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "c"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "v"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "b"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "n"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                if len(txt_str) <= 19:
                    txt_str = str(txt_str) + "m"
                    pygame.time.delay(150)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if txt_str == "triangle":
                    win.blit(triangles, (0,0))
                    pygame.display.update()
                    break
                elif txt_str == "square":
                    win.blit(squares, (0,0))
                    pygame.display.update()
                    break
                elif txt_str == "circle":
                    win.blit(circles, (0,0))
                    pygame.display.update()
                    break
                else:
                    txt_str = ""
        txt = arial2.render(txt_str, True, (0, 0, 0))
        

    
    
