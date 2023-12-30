# importing libraries
import pygame
import time
import random
from pygame import mixer
velocity = 10

start_time = time.time()


# Window size
length = 600
breadth = 600

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
dark_green=pygame.Color(1,50,32)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('SnakeGame.oi')
game_window = pygame.display.set_mode((length, breadth))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
			[90, 50],
			[80, 50],
			[70, 50]
			]
# fruit position
fruit_position = [random.randrange(1, (length//10)) * 10, 
				random.randrange(1, (length//10)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

mixer.init() 
mixer.music.load("snake_music.mp3") 
mixer.music.set_volume(0.7)   
mixer.music.play()

# initial score
points = 0

# displaying Score function
def show_score(choice, color, font, size):
	score_font = pygame.font.SysFont(font, size)
	score_surface = score_font.render('Score : {}'.format(points), True, color)
	score_rect = score_surface.get_rect()
	game_window.blit(score_surface, score_rect)


# game over function
def game_over():
	my_font = pygame.font.SysFont('times new roman', 50)
	game_over_surface = my_font.render(
		'Your Score is : {}'.format(points), True, red)
	game_over_rect = game_over_surface.get_rect()
	game_over_rect.midtop = (length/2, length/4)
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	time.sleep(4)
	pygame.quit()
	quit()


# Main Function
while True:
	
	# handling key events
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'

	# If two keys pressed simultaneously
	# we don't want snake to move into two 
	# directions simultaneously
	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Moving the snake
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	snake_body.insert(0, list(snake_position))
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		points += 1
		fruit_spawn = False
	else:
		snake_body.pop()
		
	if not fruit_spawn:
		fruit_position = [random.randrange(1, (length//10)) * 10, 
						random.randrange(1, (breadth//10)) * 10]
		
	fruit_spawn = True
	game_window.fill(green)
	
	for pos in snake_body:
		if pos in snake_body[0:4]:
		    pygame.draw.rect(game_window, dark_green,pygame.Rect(pos[0], pos[1], 10, 10))
		elif pos in snake_body[4:]:
			pygame.draw.rect(game_window, red ,pygame.Rect(pos[0], pos[1] ,10,10))
	
	
	pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

	# Game Over conditions
	if snake_position[0] < 0 or snake_position[0] > length-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > breadth-10:
		game_over()

	# Touching the snake body
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	# displaying score continuously
	show_score(1, blue, 'times new roman', 20)

	# Refresh game screen
	pygame.display.update()

	# Frame Per Second /Refresh Rate
	fps.tick(velocity)