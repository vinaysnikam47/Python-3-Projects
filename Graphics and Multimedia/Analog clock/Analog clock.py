# Simple analog clock showing current time

import turtle
import time
import winsound


# Craeation of Screen
wn = turtle.Screen()
wn.bgcolor('white')
wn.setup(width=600, height=600)
wn.title('Analog clock by Vinay')
wn.tracer(0)

# Craetion of clock face
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(4)


def draw_clock(h, m, s, pen):

	# Clock shape
	pen.up()
	pen.goto(0, 210)
	pen.setheading(180)
	pen.color('grey')
	pen.pendown()
	pen.circle(210)

	# Clock hour numbers
	pen.up()
	pen.goto(0, 0)
	pen.setheading(90)

	for i in range(12):
		pen.fd(190)
		pen.pendown()
		pen.fd(20)
		pen.up()
		pen.goto(0, 0)
		pen.rt(30)

	# Creation of Hour hand	
	pen.up()
	pen.goto(0, 0)
	pen.pendown()
	pen.pensize(6)
	pen.color('green')
	pen.setheading(90)
	angle = ((h/12)*360)+(30*m/60)+(s*30/3600)
	pen.rt(angle)
	pen.fd(70)

	# Creation of Minute hand
	pen.up()
	pen.goto(0, 0)
	pen.pendown()
	pen.pensize(4)
	pen.color('red')
	pen.setheading(90)
	angle = ((m/60)*360)+(30*s/3600)
	pen.rt(angle)
	pen.fd(100)

	# Creation of Second hand
	pen.up()
	pen.goto(0, 0)
	pen.pendown()
	pen.pensize(2)
	pen.color('blue')
	pen.setheading(90)
	angle = (s/60)*360
	pen.rt(angle)
	pen.fd(180)
	pen.pensize(4)

	
while True:    # Wrapping function 
	h = int(time.strftime('%I'))
	m = int(time.strftime('%M'))
	s = int(time.strftime('%S'))

	draw_clock(h,m,s,pen)
	winsound.PlaySound('tick.wav', winsound.SND_ASYNC)
	wn.update()
	time.sleep(1)
	pen.clear()

wn.mainloop()	
