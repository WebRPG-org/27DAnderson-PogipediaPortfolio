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
        smallest_circle_size = int(input("Enter the size of the smallest circle/distance between circles as a number: "))
    except ValueError:
        print("✗")
        continue
    except AttributeError:
        print("✗")
    else:
        print("✓")
        break

while True:
    try:
        num_circles = int(input("Enter the number of circles as a number: "))
    except ValueError:
        print("✗")
        continue
    except AttributeError:
        print("✗")
    else:
        print("✓")
        break

while True:
    try:
        outline = input("Enter a color as a word or hex for outline, or none for no outline: ")
        if outline == "none" or outline == "no":
            print("✓")
            break
        check_color(outline)
        t.color(outline)
        print("✓")
        break
    except turtle.TurtleGraphicsError:
        print("✗")
    except ValueError:
        print("✗")
        outline = None
        continue
    except AttributeError:
        outline = None
        print("✗")

while True:
    try:
        num_colors = int(input("Enter the number of colors as a number: "))
    except ValueError:
        print("✗")
        continue
    except AttributeError:
        print("✗")
    else:
        if num_colors > num_circles:
            print("✗")
            pass
        else:
            print("✓")
            break
    

colors = []
for i in range(num_colors):
    while True:
        color = input("Enter color " + str(i+1) +" as word or hex: ")
        check_color(color)
        if is_color == True:
            colors.append(color.lower())
            print("✓")
            break
        else:
            print("✗")
while True:
    try:
        speed = input("Would you like to speed up the turtle, enter yes are no: ")
        if speed.lower() == "yes" or speed.lower() == "y":
            t.speed(0)
            print("✓")
            break
        elif speed.lower() == "no" or speed.lower() == "n":
            print("✓")
            break
        else:
            print("✗")
    except turtle.TurtleGraphicsError:
        print("✗")

while True:
    try:
        show_hide = input("Would you like to show the turtle when finished, enter yes are no: ")
        if show_hide.lower() == "yes" or show_hide.lower() == "y":
            print("✓")
            break
        elif show_hide.lower() == "no" or show_hide.lower() == "n":
            print("✓")
            break
        else:
            print("✗")
    except turtle.TurtleGraphicsError:
        print("✗")

print("Drawing...")
for i in range(num_circles):
    radius = smallest_circle_size + (num_circles - i - 1) * smallest_circle_size
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
print("Finished drawing.")
turtle.done()
