import pygame
import math
pygame.init()
####

####
res = w,h = 700,700
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Paint")
####
white = (255,255,255)
black = (0,0,0)
screen.fill(white)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
color = BLUE
List = [RED,GREEN,BLUE]
####
drawingrect = 0 ### if you draw, then ==1
drawingcircle = 0
drawingsquare = 0
drawingRightTriangle = 0
drawEqualTriangle = 0
drawRhombus = 0
clock = pygame.time.Clock()
finished = False
isPressed = False
cnt = 0
while not finished:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_r]:
            color = RED
        elif pressed_keys[pygame.K_g]:
            color = GREEN
        elif pressed_keys[pygame.K_b]:
            color = BLUE
        elif pressed_keys[pygame.K_SPACE]:
            drawingrect = 1
        elif pressed_keys[pygame.K_c]:
            drawingcircle = 1
        elif pressed_keys[pygame.K_s]:
            drawingsquare = 1
        elif pressed_keys[pygame.K_t]:
            drawingRightTriangle = 1
        elif pressed_keys[pygame.K_y]:
            drawEqualTriangle = 1
        elif pressed_keys[pygame.K_u]:
            drawRhombus = 1
        ###ERASER+RECT###
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            for i in range(650,665):
                for j in range(40, 55):
                    if i == x and j == y:
                        if cnt>2:
                            cnt=0
                        color = List[cnt]
                        cnt+=1
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            for i in range(650,665):
                for j in range(1, 16):
                    if i == x and j == y:
                        color = white
            isPressed = True 
        ###ERASER###
         
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False

        if event.type == pygame.MOUSEMOTION and isPressed == True and drawingrect == drawingcircle == drawingsquare == 0:         
            (x, y) = pygame.mouse.get_pos()   # returns the position of mouse cursor
            if color == white:
                pygame.draw.rect(screen, color, (x-20,y-20,40,40))
            else:
                pygame.draw.circle( screen,color, (x, y), 10)
        
        if isPressed == True and drawingrect == 1:  
            (x, y) = pygame.mouse.get_pos()
            pygame.draw.rect(screen, color, (x-25,y-20,50,40))
            drawingrect = 0
        
        elif isPressed == True and drawingcircle == 1:  
            (x, y) = pygame.mouse.get_pos()
            pygame.draw.circle( screen,color, (x, y), 20)
            drawingcircle = 0
        
        elif isPressed and drawingsquare == 1:  
            (x, y) = pygame.mouse.get_pos()
            pygame.draw.rect( screen, color, (x-25, y-25,50,50))
            drawingsquare = 0

        elif isPressed and drawingRightTriangle == 1:  
            (x, y) = pygame.mouse.get_pos()
            pygame.draw.polygon(screen, color, [(x, y), (x, y-100), (x+70, y)])
            drawingRightTriangle = 0
        elif isPressed and drawEqualTriangle == 1:  
            (x, y) = pygame.mouse.get_pos()
            pygame.draw.polygon(screen, color, [(x, y), (x+100, y), (x+50, y-100*math.sqrt(3)//2)])
            drawEqualTriangle = 0
        elif isPressed and drawRhombus == 1:  
            (x, y) = pygame.mouse.get_pos()
            pygame.draw.polygon(screen, color, [(x, y), (x+100, y), (x+50, y-100*math.sqrt(3)//2)])
            pygame.draw.polygon(screen, color, [(x, y), (x+100, y), (x+50, y+100*math.sqrt(3)//2)])
            drawRhombus = 0
        
    pygame.draw.rect(screen, black, (650,1,15,15), 1)
    pygame.draw.rect(screen, color, (650,40,15,15))

    pygame.display.update()
    clock.tick(700)
pygame.quit()
