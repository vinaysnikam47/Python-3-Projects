# Simple snake game in python for beginners
# Use arrow keys for movement of snake

import turtle
import time
import random
import winsound

delay = 0.1

score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title('Snake Game by Vinay')
wn.bgcolor("silver")
wn.setup(width=600, height=600)
wn.tracer(0)
wn.bgpic('grass.png')


# Snake head
head = turtle.Turtle()
head.speed(1)
head.shape('square')
head.color('green')
head.penup()
head.goto(0,0)
head.direction = 'stop'

# Snake food
food = turtle.Turtle()
food.shape('circle')
food.color('darkred', 'crimson')
food.penup()
food.goto(0,100)


# Pen
pen = turtle.Turtle()
pen.shape('square')
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score : 0  High Score : 0', align = 'center', font = ('courier',20,'bold'))


segments = []

# Functions
def go_up():
	if head.direction != 'down':
	    head.direction = 'up'

def go_down():
	if head.direction != 'up':
	    head.direction = 'down'

def go_left():
	if head.direction != 'right':
	    head.direction = 'left'

def go_right():
	if head.direction != 'left':
	    head.direction = 'right'

def move():
	if head.direction == 'up':
		y = head.ycor()
		head.sety(y + 20)


	if head.direction == 'down':
		y = head.ycor()
		head.sety(y - 20)


	if head.direction == 'left':
		x = head.xcor()
		head.setx(x - 20)

	if head.direction == 'right':
		x = head.xcor()
		head.setx(x + 20)


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, key='Up')
wn.onkeypress(go_down, key='Down')
wn.onkeypress(go_left, key='Left')
wn.onkeypress(go_right, key='Right')


# Main game loop
while True:
	wn.update()

    # Check for collision with the border
	if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
		winsound.PlaySound('burst.wav', winsound.SND_ASYNC)
		time.sleep(1)
		head.goto(0, 0)
		head.direction = 'stop'

        # Clear the segments
		for segment in segments:
			segment.goto(1000, 1000)
			
        
        # Clear the segment list
		segments.clear()

		# Reset the score
		delay = 0.1
		score = 0
		pen.clear()
		pen.goto(0, 0)
		pen.write('GAME OVER', align='center', font=('courier', 25, 'bold'))
		time.sleep(1)
		pen.clear()
		pen.goto(0, 260)
		pen.write(f'Score : {score}  High Score : {high_score}', align='center',font=('courier',20,'bold'))

	# Check for collision with the food
	if head.distance(food) < 20:
		# Move food to the random position of screen
		x = random.randrange(-280, 280, 20)
		y = random.randrange(-280, 280,20)
		food.goto(x, y)

		# Add a segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape('square')
		new_segment.color('darkgreen', 'mediumseagreen')
		winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
		new_segment.penup()
		segments.append(new_segment)

		# Shrtens the delay (Increases speed of snake)
		delay -= 0.001

		score += 10

		if score > high_score:
			high_score = score

		pen.clear()
		pen.write(f'Score : {score}  High Score : {high_score}', align='center',font=('courier',20,'bold'))

	# Move the first segment first in reverse order
	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)

    # Move segment 0 to where the head is
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)

	move()

    # Check for collision with the body
	for segment in segments:
		if segment.distance(head) < 20:
			winsound.PlaySound('burst.wav', winsound.SND_ASYNC)
			time.sleep(1)
			head.goto(0, 0)
			head.direction = 'stop'

			# Clear the segment
			for segment in segments:
				segment.goto(1000, 1000)

			# CLear the segment list
			segments.clear()

			# Reset the score
			delay = 0.1
			score = 0
			pen.clear()
			pen.goto(0, 0)
			pen.write('GAME OVER', align='center', font=('courier', 25, 'bold'))
			time.sleep(1)
			pen.clear()
			pen.goto(0, 260)
			pen.write(f'Score : {score}  High Score : {high_score}', align='center',font=('courier',20,'bold'))

	time.sleep(delay)

wn.mainloop()
