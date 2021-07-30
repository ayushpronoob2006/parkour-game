import turtle
import time

# window settings
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(height=600,width=900)
wn.tracer(0)
wn.title("PARKOUR GAME")





# player
player = turtle.Turtle()
player.color("grey")
player.speed(0)
player.shape("square")
player.penup()
player.goto(-400,-250)
player.state = "ready"
player.dx = 0
player.dy = 0

#spike1
spike1 = turtle.Turtle()
spike1.color("red")
spike1.left(90)
spike1.speed(0)
spike1.shape("triangle")
spike1.penup()
spike1.goto(-150,-250)
spike1.shapesize(stretch_wid=2,stretch_len=2)

#spike2
spike2 = turtle.Turtle()
spike2.color("red")
spike2.left(90)
spike2.speed(0)
spike2.shape("triangle")
spike2.penup()
spike2.goto(150,-250)
spike2.shapesize(stretch_wid=2,stretch_len=2)

#spike3
spike3 = turtle.Turtle()
spike3.color("red")
spike3.left(90)
spike3.speed(0)
spike3.shape("triangle")
spike3.penup()
spike3.goto(0,0)
spike3.shapesize(stretch_wid=2,stretch_len=2)

#ball
ball = turtle.Turtle()
ball.color("red")
ball.speed(0)
ball.shape("circle")
ball.penup()
ball.goto(-300,220)
ball.dx = 0.5


# slab1
slab1 = turtle.Turtle()
slab1.color("white")
slab1.speed(0)
slab1.shape("square")
slab1.penup()
slab1.goto(340,-200)
slab1.shapesize(stretch_wid=1,stretch_len=12)

# slab2
slab2 = turtle.Turtle()
slab2.color("white")
slab2.speed(0)
slab2.shape("square")
slab2.penup()
slab2.goto(0,-150)
slab2.shapesize(stretch_wid=1,stretch_len=12)

# slab3
slab3 = turtle.Turtle()
slab3.color("white")
slab3.speed(0)
slab3.shape("square")
slab3.penup()
slab3.goto(-340,-100)
slab3.shapesize(stretch_wid=1,stretch_len=12)

# slab4
slab4 = turtle.Turtle()
slab4.color("white")
slab4.speed(0)
slab4.shape("square")
slab4.penup()
slab4.goto(150,-20)
slab4.shapesize(stretch_wid=1,stretch_len=30)

# slab5
slab5 = turtle.Turtle()
slab5.color("white")
slab5.speed(0)
slab5.shape("square")
slab5.penup()
slab5.goto(340,-20)
slab5.shapesize(stretch_wid=1,stretch_len=10)
slab5.dy = 0.1

# slab6
slab6 = turtle.Turtle()
slab6.color("white")
slab6.speed(0)
slab6.shape("square")
slab6.penup()
slab6.goto(-100,200)
slab6.shapesize(stretch_wid=1,stretch_len=30)

# check point
cp = turtle.Turtle()
cp.color("grey")
cp.speed(0)
cp.shape("square")
cp.penup()
cp.goto(-350,260)
cp.shapesize(stretch_wid=5,stretch_len=3)


# ground level

gl = turtle.Turtle()
gl.color("white")
gl.speed(0)
gl.shape("square")
gl.penup()
gl.goto(0,-280)
gl.shapesize(stretch_len=1000,stretch_wid=2)


# gravity
gravity = -0.01

# function
def jump():
    if player.state == "ready":
        player.dy = 1.3
        player.state = "jumping"

def right():
    if player.state == "ready":
        player.dx = 0.7

def left():
    if player.state == "ready":
        player.dx = -0.7

# keyboard binding
wn.listen()
wn.onkeypress(jump,"space")
wn.onkeypress(right,"Right")
wn.onkeypress(left,"Left")

# main game loop

while True:
    wn.update()

    player.dy += gravity

    # move the slab
    slab5.sety(slab5.ycor() + slab5.dy)

    # jump
    y = player.ycor()
    y += player.dy
    player.sety(y)
    player.state = "jumping"

    # right
    x = player.xcor()
    x += player.dx
    player.setx(x)
    player.state = "jumping"

    # left
    x = player.xcor()
    x += player.dx
    player.setx(x)
    player.state = "jumping"

    if player.ycor() < -250:
        player.sety(-250)
        player.state = "ready"

    if player.xcor() < -440:
        player.setx(-440)

    if player.xcor() > 430:
        player.setx(430)

    # platform 1

    if player.ycor() < -180 and player.ycor() > -185 and player.xcor() < slab1.xcor() + 120 and player.xcor() > slab1.xcor() - 120:
        player.sety(-180)
        player.dy = 0
        player.state = "ready"

    if player.ycor() < -210 and player.ycor() > -215 and player.xcor() < slab1.xcor() + 120 and player.xcor() > slab1.xcor() - 120:
        player.sety(-220)
        player.dy = 0
        player.state = "ready"



    if player.ycor() < -130 and player.ycor() > -135 and player.xcor() < slab2.xcor() + 120 and player.xcor() > slab2.xcor() - 120:
        player.sety(-130)
        player.dy = 0
        player.state = "ready"

    if player.ycor() < -160 and player.ycor() > -165 and player.xcor() < slab2.xcor() + 120 and player.xcor() > slab2.xcor() - 120:
        player.sety(-170)
        player.dy = 0
        player.state = "ready"



    if player.ycor() < -80 and player.ycor() > -85 and player.xcor() < slab3.xcor() + 120 and player.xcor() > slab3.xcor() - 120:
        player.sety(-80)
        player.dy = 0
        player.state = "ready"

    if player.ycor() < -110 and player.ycor() > -115 and player.xcor() < slab3.xcor() + 120 and player.xcor() > slab3.xcor() - 120:
        player.sety(-120)
        player.dy = 0
        player.state = "ready"



    if player.ycor() < 0 and player.ycor() > -5 and player.xcor() < slab4.xcor() + 300 and player.xcor() > slab4.xcor() - 300:
        player.sety(-0)
        player.dy = 0
        player.state = "ready"

    if player.ycor() < -10 and player.ycor() > -15 and player.xcor() < slab4.xcor() + 300 and player.xcor() > slab4.xcor() - 300:
        player.sety(-20)
        player.dy = 0
        player.state = "ready"

    if slab5.ycor() > 200:
        slab5.dy = -0.1

    if slab5.ycor() < -20:
        slab5.dy = 0.1

    if player.ycor() < slab5.ycor() + 20 and player.ycor() > slab5.ycor() -20 and player.xcor() < slab5.xcor() + 120 and player.xcor() > slab5.xcor() - 120:
        player.sety(slab5.ycor() + 20)
        player.state = "ready"



    if player.ycor() > 215 and player.ycor() < 220 and player.xcor() < slab6.xcor() + 300 and player.xcor() > slab6.xcor() - 300:
        player.sety(220)
        player.dy = 0
        player.state = "ready"

    if player.ycor() > 190 and player.ycor() < 195 and player.xcor() < slab6.xcor() + 300 and player.xcor() > slab6.xcor() - 300:
        player.sety(185)
        player.dy = 0
        player.state = "ready"

    if player.ycor() < 300 and player.ycor() > 210 and player.xcor() < cp.xcor() + 20 and player.xcor() > cp.xcor() - 20:
        player.goto(-400,-250)
        player.dy = 0
        player.state = "jumping"
        time.sleep(2)


    if player.ycor() < -220 and player.ycor() > -270 and  player.xcor() > spike1.xcor() - 5 and player.xcor() < spike1.xcor() + 5:
        time.sleep(2)
        player.goto(-400,-250)

    if player.ycor() < -220 and player.ycor() > -270 and  player.xcor() > spike2.xcor() - 5 and player.xcor() < spike2.xcor() + 5:
        time.sleep(2)
        player.goto(-400,-250)


    if player.ycor() < 20 and player.ycor() > -10 and  player.xcor() > spike3.xcor() - 5 and player.xcor() < spike3.xcor() + 5:
        time.sleep(2)
        player.goto(-400,-250)

    # move the ball
    ball.setx(ball.xcor() + ball.dx)

    # border check
    if ball.xcor() > 200:
        ball.setx(-300)

    if player.ycor() < 230 and player.ycor() > 200 and player.xcor() < ball.xcor() + 1 and player.xcor() > ball.xcor() - 1:
        time.sleep(2)
        player.goto(-400,-250)




