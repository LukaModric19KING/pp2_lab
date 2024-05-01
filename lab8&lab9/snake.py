import pygame
import random
pygame.init()

snake_speed = 10
res = w,h = 700,700
black = (0, 0, 0)
white = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.display.set_caption('snake')
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

snake_pos = [50, 50]
snake_body = [[50, 50],[40, 50]]
fruit_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]
fruit = True

startdir = 'RIGHT'
direct = startdir

def Score(score, level):
    basicfont = pygame.font.SysFont(None, 30)
    score_surface = basicfont.render('Your Score : ' + str(score), True, white)
    score_surface2 = basicfont.render('Your Level : ' + str(level), True, white)
    screen.blit(score_surface, (0,0))
    screen.blit(score_surface2, (200,0))

score = 0
basicFontForText = pygame.font.SysFont(None, 30)
cnt=0
finished = False
lll = 0
level = 0
while not finished:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				direct = 'UP'
			if event.key == pygame.K_DOWN:
				direct = 'DOWN'
			if event.key == pygame.K_LEFT:
				direct = 'LEFT'
			if event.key == pygame.K_RIGHT:
				direct = 'RIGHT'

	if direct == 'UP' and startdir != 'DOWN':
		startdir = 'UP'
	if direct == 'DOWN' and startdir != 'UP':
		startdir = 'DOWN'
	if direct == 'LEFT' and startdir != 'RIGHT':
		startdir = 'LEFT'
	if direct == 'RIGHT' and startdir != 'LEFT':
		startdir = 'RIGHT'

	
	if startdir == 'UP':
		snake_pos[1] -= 10
	if startdir == 'DOWN':
		snake_pos[1] += 10
	if startdir == 'LEFT':
		snake_pos[0] -= 10
	if startdir == 'RIGHT':
		snake_pos[0] += 10

	
	snake_body.insert(0, list(snake_pos)) #add [0]
	if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
		score += 1
		cnt+=1
		fruit = False
	else:
		snake_body.pop() #delete [last]
	screen.fill(black)
	if not fruit:
		fruit_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]	
	fruit = True
	
	for pos in range(len(snake_body)):
		if pos == 0:
			pygame.draw.circle(screen, RED, (snake_body[pos][0], snake_body[pos][1]), 7.5)
		else:
			pygame.draw.circle(screen, GREEN, (snake_body[pos][0], snake_body[pos][1]), 7.5)
	pygame.draw.circle(screen, white, (fruit_pos[0], fruit_pos[1]), 7.5)

	if snake_pos[0] < 0 or snake_pos[0] > w-10:
		exit()
	if snake_pos[1] < 0 or snake_pos[1] > h-10:
		exit()

	
	if cnt>=3:
		snake_speed+=3
		lll+=1
		cnt=0
	Score(score, lll)
	pygame.display.update()
	clock.tick(snake_speed)
pygame.quit()
