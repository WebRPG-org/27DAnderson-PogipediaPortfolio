import turtle

t = turtle.Turtle()
is_color = None
outline = None

def check_color(enter):
    try:
        global is_color
        t.fillcolor(enter)
        t.fillcolor("black")
        is_color = True
    except turtle.TurtleGraphicsError:
        is_color = False
    except ValueError:
        is_color = False
    except AttributeError:
        is_color = False

while True:
    try:
        smallest_circle_size = turtle.textinput("Input","Enter the size of the smallest circle/distance between circles as a number: ")
    except ValueError:
        continue
    except AttributeError:
        pass
    else:
        break

while True:
    try:
        num_circles = turtle.textinput("Input","Enter the number of circles as a number: ")
    except ValueError:
        continue
    except AttributeError:
        pass
    else:
        break

while True:
    try:
        outline = turtle.textinput("Input","Enter a color as a word or hex for outline, or none for no outline: ")
        if outline == "none" or outline == "no":
            break
        check_color(outline)
        t.color(outline)
        break
    except turtle.TurtleGraphicsError:
        pass
    except ValueError:
        outline = None
        continue
    except AttributeError:
        outline = None

while True:
    try:
        num_colors = int(turtle.textinput("Input","Enter the number of colors as a number: "))
        if int(num_colors) > int(num_circles):
            pass
        elif int(num_colors) <= int(num_circles):
            break
    except ValueError:
        continue
    except AttributeError:
        pass
    else:
        if int(num_colors) > int(num_circles):
            pass
        else:
            break
    

colors = []
for i in range(int(num_colors)):
    while True:
        color = turtle.textinput("Input","Enter color " + str(i+1) +" as word or hex: ")
        check_color(color)
        if is_color == True:
            colors.append(color.lower())
            break
        else:
            pass
while True:
    try:
        speed = turtle.textinput("Input","Would you like to speed up the turtle, enter yes are no: ")
        if speed.lower() == "yes" or speed.lower() == "y":
            t.speed(0)
            break
        elif speed.lower() == "no" or speed.lower() == "n":
            break
        else:
            pass
    except turtle.TurtleGraphicsError:
        pass

while True:
    try:
        show_hide = turtle.textinput("Input","Would you like to show the turtle when finished, enter yes are no: ")
        if show_hide.lower() == "yes" or show_hide.lower() == "y":
            break
        elif show_hide.lower() == "no" or show_hide.lower() == "n":
            break
        else:
            pass
    except turtle.TurtleGraphicsError:
        pass
for i in range(int(num_circles)):
    radius = int(smallest_circle_size) + (int(num_circles) - i - 1) * int(smallest_circle_size)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.fillcolor(colors[i % len(colors)])
    if outline.lower() == "none":
        t.color(colors[i % len(colors)])
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
if show_hide.lower() =="no" or show_hide.lower() == "no":
    t.hideturtle()
else:
    t.color("black")
turtle.done()

