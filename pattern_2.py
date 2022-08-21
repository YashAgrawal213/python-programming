import turtle
import colorsys
t= turtle.Turtle()
s= turtle.Screen()
s.bgcolor("black")
t.speed(0)
n=40
h=0
for i in range(460):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=1/n
    t.color(c)
    t.left(252)
    for j in range(5):
        t.forward(300)
        t.left(150)