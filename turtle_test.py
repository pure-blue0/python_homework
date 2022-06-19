import sys
import turtle
import time

i = 0

def penInit():
    global i
    i = 0
    turtle.reset()
    turtle.color('violet')
    turtle.pensize(10)
    turtle.speed(10)

def drawPrgress():
    global i
    i += 1
    print("\r progress:{}% | {}{} |".format(i * 20, "*" * i * 20, "." * (5 - i) * 20), end="")
    #sys.stdout.flush()
    time.sleep(0.5)

def drawSnake(rad, angle, len, neckrad):
        for i in range(len):
            turtle.circle(rad, angle)
            turtle.circle(-rad, angle)
        turtle.circle(rad, angle/2)
        turtle.fd(rad)
        turtle.circle(neckrad+1,180)
        turtle.fd(rad*2/3)

def drawLine(x,y,angle,length):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.setheading(angle)
    turtle.pendown()
    turtle.forward(length)
    turtle.penup()
    drawPrgress()

    #sys.stdout.flush()


def drawCharacter():
    penInit()
    drawLine(-100,0,0,200)
    drawLine(0,100,-90,100)
    drawLine(0,0,-120,120)
    drawLine(0,0,-60,120)
    drawPrgress()
    #turtle.exitonclick()


if __name__ == "__main__":
    drawCharacter()
    #progress_bar()


