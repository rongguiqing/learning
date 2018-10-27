#pythondraw 绘制一条蟒蛇
'''
import turtle
turtle.setup(650, 350)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()

import turtle as t
t.setup(800, 400)
t.penup()
t.fd(-40)
t.left(90)
t.fd(40)
t.right(90)
t.pendown()
t.pensize(3)
t.pencolor("black")
for i in range(4):
    t.fd(80)
    t.right(90)
t.done()
'''
import turtle as t
t.screensize(800, 800, "green")
t.pencolor("black")
t.pensize(5)
for i in range(9):
    t.fd(150)
    t.left(80)
t.done()