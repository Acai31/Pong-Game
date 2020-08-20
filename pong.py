import turtle
import sys
import time

wn = turtle.Screen()
wn.title("Pong copied from freecodecamp")
wn.bgcolor("black")
wn.setup(width = 750, height = 600)
wn.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(stretch_wid = 5, stretch_len = 1)
paddleA.color("grey")
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid = 5, stretch_len = 1)
paddleB.color("grey")
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {}  Player B: {}  ".format(scoreA, scoreB), align = "center", font = ("Courier", 20, "normal"))

# When game ends write game over screen: 
over = turtle.Turtle()
over.speed(0)
over.color("white")
over.penup()
over.hideturtle()
over.goto(0, 240)
# first write out how to win game lol
over.write("First to 7 points wins!", align = "center", font = ("Courier", 15, "normal"))
# game over called should be at very bottom of this file I think

# Credits and stuff? 
credit = turtle.Turtle()
credit.speed(0)
credit.color("tan")
credit.penup()
credit.hideturtle()
credit.goto(0, -275)
credit.write("Based on freeCodeCamp's Pong game tutorial, remixed by Alex Cheung", align = "center", font = ("Courier", 12, "normal"))

# Function
def paddleAUp():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleADown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddleBUp():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleBDown():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


#Keyboard binding
wn.listen()
wn.onkeypress(paddleAUp, "w")
wn.onkeypress(paddleADown, "s")
wn.onkeypress(paddleBUp, "Up")
wn.onkeypress(paddleBDown, "Down")

# Main game loop
while True: 
    wn.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}  ".format(scoreA, scoreB), align = "center", font = ("Courier", 20, "normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}  ".format(scoreA, scoreB), align = "center", font = ("Courier", 20, "normal"))

    # Paddle and ball touches
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

    # When the first person scores 7 points to end the game
    # Check if anyone has won the game
    if scoreA > 6 or scoreB > 6: 
        ball.reset()
        paddleA.reset()
        paddleB.reset()
        over.clear()
        over.goto(0, 0)
        # check if player A won or player B 
        if scoreA > scoreB:
            over.write("Player A has won! Congratulations!!", align = "center", font = ("Courier", 25, "normal"))
        else: 
            over.write("Player B has won! Congratulations!!", align = "center", font = ("Courier", 25, "normal"))
        # wait 5 seconds before closing the game window because I don't want to close it every single time lol
        time.sleep(5)
        sys.exit()

