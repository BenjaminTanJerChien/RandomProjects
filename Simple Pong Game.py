#simple pong game
import turtle
import time

wn = turtle.Screen()
wn.title("Pong by me")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
pada = turtle.Turtle()
pada.speed(0)
pada.shape("square")
pada.color("white")
pada.shapesize(stretch_wid=5, stretch_len=1)
pada.penup()
pada.goto(-350, 0)

#Paddle B
padb = turtle.Turtle()
padb.speed(0)
padb.shape("square")
padb.color("white")
padb.shapesize(stretch_wid=5, stretch_len=1)
padb.penup()
padb.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

def pada_up():
    y = pada.ycor()
    y += 20
    pada.sety(y)

def pada_down():
    y = pada.ycor()
    y -= 20
    pada.sety(y)

def padb_up():
    y = padb.ycor()
    y += 20
    padb.sety(y)

def padb_down():
    y = padb.ycor()
    y -= 20
    padb.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(pada_up, "w")
wn.onkeypress(pada_down, "s")
wn.onkeypress(padb_up, "Up")
wn.onkeypress(padb_down, "Down")


score_a = 0
score_b = 0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(f"Player A: {score_a}   |   Player B: {score_b}", align="center", font=("Arial", 24, "normal" ))

#main game loop
while True:
    try: 
        time.sleep(0.0001 / (score_a + score_b))
    except: 
        time.sleep(0.0001)
    wn.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1         

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write(f"Player A: {score_a}   |   Player B: {score_b}", align="center", font=("Arial", 24, "normal" ))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write(f"Player A: {score_a}   |   Player B: {score_b}", align="center", font=("Arial", 24, "normal" ))



    if ball.xcor() > 340 and ball.ycor() < padb.ycor() + 50 and ball.ycor() > padb.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1

    elif ball.xcor() < -340 and ball.ycor() < pada.ycor() + 50 and ball.ycor() > pada.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
    


