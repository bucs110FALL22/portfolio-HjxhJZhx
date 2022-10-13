import random
import turtle


t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')

t.speed(0)

distance = 10
angle = 90
is_in_screen = True

colors = ["green", "blue", "purple"]

while is_in_screen:
    coin = random.randrange(0, 2)
    if coin:           # heads
        t.right(angle)
    else:                      # tails
        t.left(angle)
    t.forward(distance)
    # t.forward(10) #magic number/data
    
    turtleX = t.xcor()
    turtleY = t.ycor()
    #x, y = t.pos()
    
    x_range = wn.window_width()/2
    y_range = wn.window_height()/2
    
    t.color(colors[0])
    
    colors.append(colors.pop(0))
    
    if abs(turtleX) > x_range or abs(turtleY) > y_range:
        is_in_screen = False
        
wn.bgcolor("yellow")
wn.exitonclick()
