
import turtle

window = turtle.Screen()
window.title("PingPong")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

#Score
score_a = 0
score_b = 0

#create left paddle
leftpaddle = turtle.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("black")
leftpaddle.shapesize(stretch_wid=6, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

#create right paddle
rightpaddle = turtle.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("black")
rightpaddle.shapesize(stretch_wid=6, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

#create ball
ball = turtle.Turtle()
ball.speed(2)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = -0.4

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))

#Function to move left paddle up
def leftpaddle_up():
    y=leftpaddle.ycor()
    y=y+50
    leftpaddle.sety(y)

#Function to move left paddle down
def leftpaddle_down():
    y=leftpaddle.ycor()
    y=y-50
    leftpaddle.sety(y)

#function to move right paddle up
def rightpaddle_up():
    y=rightpaddle.ycor()
    y+=50
    rightpaddle.sety(y)

#function to move right paddle down
def rightpaddle_down():
    y=rightpaddle.ycor()
    y-=50
    rightpaddle.sety(y)

#keyboard binding
window.listen()
window.onkeypress(leftpaddle_up, "w")   
window.onkeypress(leftpaddle_down, "s")
window.onkeypress(rightpaddle_up, "Up")
window.onkeypress(rightpaddle_down, "Down") 

#Main game loop
while True:
    window.update()
    
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border setup
    #bottom and up
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #left and right
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        

    #Collision with the paddles and ball
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    #game over
    if score_a == 5:
        pen.clear()
        ball.dx = 0
        ball.dy = 0
        leftpaddle.goto(-350, 0)
        rightpaddle.goto(350, 0)
        pen.write("Player A wins!", align="center", font=("Courier", 32, "normal"))

    if score_b == 5:
        pen.clear()
        ball.dx = 0
        ball.dy = 0
        leftpaddle.goto(-350, 0)
        rightpaddle.goto(350, 0)
        pen.write("Player B wins!", align="center", font=("Courier", 32, "normal"))

    