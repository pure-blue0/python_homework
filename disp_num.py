import os
import turtle
import datetime

fort = "FZYaoTi"
def penInit():
    turtle.reset()
    turtle.color('red')
    turtle.pensize(8)
    turtle.speed(-1)

def drawLine(x,y,angle,length):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.setheading(angle)
    turtle.pendown()
    turtle.forward(length)
    turtle.penup()

def drawDigit(x,y,digit):
    length = 60
    bias = 5
    turtle.color('red')
    turtle.pensize(8)
    if digit in [0, 2, 3, 5, 6, 7, 8, 9]:drawLine(x, y, 0, length)
    if digit in [2, 3, 4, 5, 6, 8, 9]:drawLine(x, y-length, 0, length)
    if digit in [0, 2, 3, 5, 6, 8, 9]:drawLine(x, y-length*2, 0, length)
    if digit in [0, 4, 5, 6, 8, 9]:drawLine(x, y, -90, length)
    if digit in [0, 1, 2, 3, 4, 7, 8, 9]:drawLine(x+length, y, -90, length)
    if digit in [0, 2, 6, 8]:drawLine(x, y-length, -90, length)
    if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9]:drawLine(x+length, y-length, -90, length)
    turtle.color('white')
    turtle.pensize(7)
    drawLine(x - 5, y + 5, -45, length*1.7)
    drawLine(x - 5, y - length + 5, -45, length*1.7)
    drawLine(x - 5, y - length - 5, 45, length*1.7)
    drawLine(x - 5, y - 2*length - 5, 45, length*1.7)

def dispDigit():
    penInit()
    digit = input("请输入一个数字：")
    x=-500
    y=60
    for i in digit:
        drawDigit(x, y, eval(i))
        # try:drawDigit(x,y,eval(i))
        # except NameError:
        #     print("输入的数据类型有误！")
        #     break
        # except:
        #     print("其他错误")
        #     print(digit)
        #     break
        x = x + 80
    #turtle.exitonclick()

def dispDate(date):
    global fort
    penInit()
    x = -500
    y = 60
    for i in date:
        if i == '-':
            turtle.setposition(x, -y)
            turtle.pendown()
            turtle.color('red')
            turtle.write('年', font=(fort, 80, "normal"))
            x = x + 120
        elif i == '=':
            turtle.setposition(x, -y)
            turtle.pendown()
            turtle.color('red')
            turtle.write('月', font=(fort, 80, "normal"))
            x = x + 120
        elif i == '+':
            turtle.setposition(x, -y)
            turtle.pendown()
            turtle.color('red')
            turtle.write('日', font=(fort, 80, "normal"))
            x = x + 120

        else:
            try:
                drawDigit(x, y, eval(i))
            except NameError:
                print("输入的数据类型有误！")
                break
            except:
                print("其他错误")
                break
            x = x + 80
    #turtle.exitonclick()


if __name__ == "__main__":
    dispDigit()
    date = datetime.datetime.now().strftime('%Y-%m=%d+')
    #print(date)
    dispDate(date)
    turtle.mainloop()
