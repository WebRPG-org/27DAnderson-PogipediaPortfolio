import turtle
import colorsys

def get_mouse_click_coor_1(x, y):
    t.goto(x, y)

def get_mouse_click_coor_2(x, y):
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.pendown()

def get_mouse_click_coor_3(x, y):
    global s
    global v
    global h
    h += 0.05
    if h > 1:
        h = 0.01
    s = 1
    v = 1
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    t.pencolor(r, g, b)
    color.pencolor(r, g, b)
    color.clear()
    #color.begin_fill()
    color.circle(10)
    #color.end_fill()

h = 0.01
s = 1
v = 1
r, g, b = colorsys.hsv_to_rgb(h, s, v)

t = turtle.Turtle()
color = turtle.Turtle()
color.speed(0)
color.hideturtle()
color.color("red")
color.penup()
color.goto(-310, 235)
color.pendown()
#color.begin_fill()
color.circle(10)
#color.end_fill()

t.pencolor(r, g, b)

t.speed(0)

t.hideturtle()

turtle.onscreenclick(get_mouse_click_coor_1, 1)
turtle.onscreenclick(get_mouse_click_coor_2, 2)
turtle.onscreenclick(get_mouse_click_coor_3, 3)

turtle.done()
