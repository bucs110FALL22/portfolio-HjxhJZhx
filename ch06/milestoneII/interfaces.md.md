# Final Project Milestone #2

[Final Project Description](https://docs.google.com/document/d/1j3zgypVjPjzXl4pL1_Wpjvp3GLCW9zcFydkwUjNfNUA/edit?usp=sharing)

Complete this document in **your** portfolio (CH 6). 

Let's decide on our Final project. Select the idea from Milestone 1 that seems the most interesting to you.

Each class is a model of some real world object. We often refer to data classes as the ***models*** in a GUI program. Your models represent your application data.

Given what you have learned about classes on Chapter 6, describe the ***interface only*** of 3 classes you think you might need for your project.

*For example*, if you want to create a space invaders type game, you would need a class to represent the ship, which could have an interface such as: 

* class ship
    * moveLeft()
    * moveRight()
    * shoot()

***

Come up with interfaces fot 3 possible classes you think you may need. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

<>

## Class Interface 2

< class Point:
	def __init__(self,x=1, y=0,color="yellow"):
		self.x = x
		self.y = y 
		if color == "red":
			print("you are wrong")
			color = "pink"
			self.color = color
			
			p1 = Point()
			print(p1.x,p1.y, p1.color, type(p1))
			p2 = Point(x=5, y=2,color="pink")
			print(p2.x, p2.y, p2.color, type(p2)) >

## Class Interface 3

< class Point(object):
  def__init__(self,x,y)
  self.X = x
  self.Y = y

  def move(self, dx,dy):
    self.X = self.X + dx
    self.Y = self.Y + dy
def test point(x=0,y=0):
p1 = point(x,y)
print p1
p2 = Point(x,0)
print p2
  