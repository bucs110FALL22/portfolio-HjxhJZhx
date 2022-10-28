import turtle 

t = turtle 

t.setup(800,400,200,200)
t.pensize(10)
t.pencolor("black")
t.bgcolor("white")


t.penup()
t.goto(-80,-80)
t.pendown()
t.seth(75)
t.fd(20)

t.penup()
t.bk(20)
t.seth(0)
t.fd(80)
t.pendown()
t.seth(105)
t.fd(40)

t.penup()
t.seth(180)
t.fd(40)
t.seth(90)
t.pencolor("orange")
t.pendown()
t.circle(18,180)
t.left(25)
t.circle(80,40)

t.penup()
t.seth(115)
t.circle(80,40)
t.seth(90)
t.circle(-18,180)
t.seth(90)
t.pendown()
t.circle(-18,180)
t.right(25)
t.circle(-80,40)
t.pendown()
t.seth(180)
t.fd(40)
t.seth(90)
t.circle(-18,180)
t.seth(90)
t.pendown()
t.penup()
t.goto(-85,-30)


t.penup()
t.goto(-85,-30)
t.seth(160)
t.pencolor("black")
t.pendown()
t.circle(-105,320)

t.penup()
t.goto(-85,75)
t.seth(90)
t.pendown()

t.begin_fill()
t.circle(15,360)
t.end_fill()

t.penup()
t.goto(-90,70)
t.pendown()

t.color("white","white")

t.begin_fill()
t.circle(3,360)
t.end_fill()

t.penup()
t.goto(-100,79)
t.pendown()

t.begin_fill()
t.circle(3,360)
t.end_fill()

t.penup()
t.goto(10,73)
t.pencolor("black")
t.pendown()

t.color("black","black")
t.begin_fill()
t.circle(15,360)
t.end_fill()

t.color("red","Pink")
t.penup()

t.goto(5,68)

t.pencolor("white")
t.pendown()
t.begin_fill()
t.circle(3,360)
t.end_fill()

t.penup()
t.goto(-5,77)
t.pendown()

t.begin_fill()
t.circle(3,360)
t.end_fill()

t.penup()
t.goto(-80,20)
t.right(45)
t.pencolor("red")
t.pendown()
t.fd(10)
t.penup()
t.bk(10)
t.seth(0)
t.pendown()
t.fd(55)
t.penup()
t.seth(120)
t.pendown()
t.fd(13)

t.penup()
t.bk(13)
t.seth(180)
t.fd(42)
t.seth(-95)

t.color("black","pink")

t.begin_fill()
t.fd(20)
t.circle(15,190)
t.right(15)
t.fd(17)
t.end_fill()

  
t.penup()
t.goto(-300,-150)
t.pensize(5)
t.pendown()
def drawFace(t):
  print("plase give me a hundred on the midterm.")
  drawFace(t)

t.penup()
t.goto(-60,-70)
t.pencolor("green")
t.pendown()
t.write("",font= ("Courier",15,"bold"))
t.done()







