# Simple space invader game
# Press space bar to fire bullet
# Press left and right arrow keys for movement of player 


import turtle
import math
import time
import random
import winsound


# Setup the screen
wn = turtle.Screen()
wn.bgcolor('silver')
wn.title('SPACE INVADERS')
wn.setup(width=650, height=650)
wn.bgpic('bg.png')

# Registering shapes of player and enemy
turtle.register_shape('invader.gif')
turtle.register_shape('space_ship.gif')
turtle.register_shape('bullet.gif')

# Drawing border
border_pen = turtle.Turtle()
border_pen.hideturtle()
border_pen.speed(0)
border_pen.penup()
border_pen.goto(-300, -300)
border_pen.pensize(3)
border_pen.pendown()
for i in range(4):
	border_pen.fd(600)
	border_pen.lt(90)

# Creation of player
player = turtle.Turtle()
player.color('darkblue', 'blue')
player.shape('space_ship.gif')
player.penup()
player.speed(0)
player.shapesize(1.25, 1.25)
player.setposition(0, -260)
player.setheading(90)

player_speed = 15

# Creation of enemy
number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color('crimson', 'red')
	enemy.penup()
	enemy.shape('invader.gif')
	enemy.speed(0)
	x = random.randint(-200, 250)
	y = random.randint(100, 230)
	enemy.setposition(x, y)

enemy_speed = 2

# Player's weapon bullet creation
bullet = turtle.Turtle()
bullet.color('red')
bullet.shape('bullet.gif')
bullet.setheading(90)
bullet.speed(0)
bullet.penup()
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 20
bullet_state = 'ready'

# Scoring system
score = 0
scoring_pen = turtle.Turtle()
scoring_pen.color('white')
scoring_pen.penup()
scoring_pen.goto(0, 260)
scoring_pen.hideturtle()
scoring_pen.write(f'Score : {score}', align='center', font=('courier', 20, 'bold'))


# Player move functions
def player_move_right():
	x = player.xcor()
	x += player_speed
	if x > 280:
		x = 280
	player.setx(x)


def player_move_left():
	x = player.xcor()
	x -= player_speed
	if x < -280:
		x = -280
	player.setx(x)


# Function for firing bullet
def fire_bullet():

	global bullet_state
	if bullet_state == 'ready':
		bullet_state = 'fire'
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()
		winsound.PlaySound('bullet.wav', winsound.SND_ASYNC)
		

# check for collision function
def is_collision(t1, t2):
	distance = math.sqrt(math.pow((t1.xcor()-t2.xcor()), 2)+math.pow((t1.ycor()-t2.ycor()), 2))
	if distance < 25:
		return True
	else:
		return False


# Commands for keyboard and game control bindings
wn.listen()
wn.onkeypress(player_move_right, key='Right')
wn.onkeypress(player_move_left, key='Left')
wn.onkeypress(fire_bullet, key='space')


while True:    # Wrapping function
	for enemy in enemies:
		x = enemy.xcor()
		x += enemy_speed
		enemy.setx(x)

		# Enemy movement to left and down
		if x > 280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemy_speed *= -1 

		# Enemy movement to right
		if x < -280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemy_speed *= -1

		# Collision check for bullet and enemy
		if is_collision(bullet, enemy):
			bullet.hideturtle()
			winsound.PlaySound('burst.wav', winsound.SND_ASYNC)
			bullet_state = 'ready'
			bullet.setposition(0, -400)
			x = random.randint(-200, 250)
			y = random.randint(100, 230)
			enemy.setposition(x, y)
			score += 10
			scoring_pen.clear()
			scoring_pen.write(f'Score : {score} ', align='center', font=('courier', 20, 'bold'))

		# Collision check for player and enemy
	if enemy.ycor() < -270:
		time.sleep(2)
		winsound.PlaySound('tada.wav', winsound.SND_ASYNC)
		enemy.hideturtle()
		player.hideturtle()
		scoring_pen.clear()
		scoring_pen.goto(0, 0)
		scoring_pen.write(f'GAME OVER', align='center', font=('courier', 25, 'bold'))

	# Firing bullet
	if bullet_state == 'fire':
		y = bullet.ycor()
		y += bullet_speed
		bullet.sety(y)

	if bullet.ycor() > 275:
		bullet.hideturtle()
		bullet_state = 'ready'

delay = input('Press enter to exit')
