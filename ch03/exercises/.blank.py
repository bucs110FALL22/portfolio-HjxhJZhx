import turtle


wn = turtle.Screen()
franklin = turtle.Turtle()
franklin.shape('turtle')
width = input("what is the width of one side?")
width = int(width)
length = int(input("what is the length of one side?"))
for s in range(2):
    franklin.forward(width)
    franklin.right(90)
    franklin.forward(length)
    franklin.right(90)
wn.exitonclick()