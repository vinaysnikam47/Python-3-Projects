# Simple pong game for two players
# Player 1 - Press 'W' and 'S' keys for movement 
# Player 2 - Press 'Up arrow' and 'Down arrow' keys for movement
# Player scoring 100 will win


import turtle
import time
import winsound


# Window creation
wn = turtle.Screen()
wn.title('Pong game by Vinay')
wn.bgcolor('silver')
wn.setup(width=800, height=600)
wn.bgpic('bg.png')
wn.tracer(0)

# Border line
bl = turtle.Turtle()
bl.pensize(4)
bl.hideturtle()
bl.penup()
bl.goto(-398, -298)
bl.pendown()
for i in range(2):
    bl.fd(796)
    bl.lt(90)
    bl.fd(596)
    bl.lt(90)

# Scoring
player_1_score = 0
player_2_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write('Player 1 Score : 0   Player 2 Score : 0', align='center', font=('courier', 18, 'bold'))

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color('darkgreen', 'mediumseagreen')
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color('darkblue', 'mediumslateblue')
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(100)
ball.color('darkred', 'crimson')
ball.shape('circle')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = -0.25


# Paddle A movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y > 240:
        y = 240
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y < -240:
        y = -240
    paddle_a.sety(y)


# Paddle B movement
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y > 240:
        y = 240
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if y < -240:
        y = -240
    paddle_b.sety(y)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, key='w')
wn.onkeypress(paddle_a_down, key='s')
wn.onkeypress(paddle_b_up, key='Up')
wn.onkeypress(paddle_b_down, key='Down')

# Main game loop
while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        winsound.PlaySound('burst.wav', winsound.SND_ASYNC)
        time.sleep(2)
        ball.goto(0, 0)
        player_1_score += 10
        pen.clear()
        if player_1_score > 90:
            pen.goto(0, 0)
            winsound.PlaySound('tada.wav', winsound.SND_ASYNC)
            pen.color('deeppink')
            pen.write('Player 1 Wins..!!', align='center', font=('courier', 25, 'bold'))
            time.sleep(3)
            pen.clear()
            pen.goto(0, 260)
            pen.color('black')
            player_1_score = 0
            player_2_score = 0
            pen.write(f'Player 1 Score : {player_1_score}   Player 2 Score : {player_2_score}',
                      align='center', font=('courier', 18, 'bold'))
            ball.dx *= -1
        else:
            pen.write(f'Player 1 Score : {player_1_score}   Player 2 Score : {player_2_score}', align='center',
                      font=('courier', 18, 'bold'))
            ball.dx *= -1

    if ball.xcor() < -390:
        winsound.PlaySound('burst.wav', winsound.SND_ASYNC)
        time.sleep(2)
        ball.goto(0, 0)
        player_2_score += 10
        pen.clear()
        if player_2_score > 90:
            pen.goto(0, 0)
            pen.color('deeppink')
            winsound.PlaySound('tada.wav', winsound.SND_ASYNC)
            pen.write('Player 2 Wins..!!', align='center', font=('courier', 25, 'bold'))
            time.sleep(3)
            pen.clear()
            pen.goto(0, 260)
            pen.color('black')
            player_1_score = 0
            player_2_score = 0
            pen.write(f'Player 1 Score : {player_1_score}   Player 2 Score : {player_2_score}', align='center',
                      font=('courier', 18, 'bold'))
            ball.dx *= -1
        else:
            pen.write(f'Player 1 Score : {player_1_score}   Player 2 Score : {player_2_score}', align='center',
                      font=('courier', 18, 'bold'))
            ball.dx *= -1

    # Collision with paddle
    if (340 < ball.xcor() < 350) and ball.ycor() in range(paddle_b.ycor() - 50, paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if (-350 < ball.xcor() < -340) and ball.ycor() in range(paddle_a.ycor() - 50, paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
