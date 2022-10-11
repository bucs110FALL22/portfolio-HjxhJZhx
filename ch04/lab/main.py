import pygame
import random
import math 

BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)

pygame.init()

screen_width=400
screen_height=400
screen=pygame.display.set_mode((screen_width,screen_height))

width = screen_width
height = screen_height
x = 0
y = 0

screen.fill("blue")
#def drawingfuncition(x,y,width,height):
#pygame.draw.circle(200,200,200,200),[x,y,width,height]
circle_x = width/2 + x
circle_y = height/2 + y
if height < width:
  radius = height/2
else:
  radius = width/2
pygame.draw.circle(screen,(RED),(circle_x,circle_y),(radius))
pygame.draw.line(screen,(BLACK),(0,circle_y),(width,circle_y))
pygame.draw.line(screen,(BLACK),(circle_x,0),(circle_x,height))            

pygame.display.update()

for i in range(10):
  x = random.randint(0,width)
  y = random.randint(0,height)
  distance_from_center = math.hypot(x - circle_x, y - circle_y) #the distance formula
  is_in_circle = distance_from_center <= radius
  if is_in_circle:
    color = GREEN
  else:
    color= YELLOW
  pygame.draw.circle(screen,(color),(x,y),(3))
  pygame.display.update()

Player1 = ("Red")
Player2 = ("Blue")  
redbox = pygame.draw.rect(screen,RED,(0,0,width/2,height))
bluebox = pygame.draw.rect(screen,BLUE,(width/2,0,width/2,height))
input("Please choose player Red or Blue by using left and left and right mouse buttom")
pygame.display.update()
exit_game= True
while not exit_game:
  for event in pygame.event.get():
    if event.type ==pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      if redbox.collidepoint(pos):
        player=Player1
      if bluebox.collidepoint(pos):
        player=Player2

screen.fill("black")
pygame.draw.circle(screen,(GREEN),(circle_x,circle_y),(radius))
pygame.draw.line(screen,(BLACK),(0,circle_y),(width,circle_y))
pygame.draw.line(screen,(BLACK),(circle_x,0),(circle_x,height))            

pygame.display.update()

score1 = 0 
score2 = 0
for i in range(10):
  x1 = random.randint(0,width)
  y1 = random.randint(0,height)
  distance_from_center = math.hypot(x1 - circle_x, y1 - circle_y) 
  is_in_circle = distance_from_center <= radius
  if is_in_circle:
    score1+=1
    color = RED
  else:
    color = YELLOW
  pygame.draw.circle(screen,(color),(x1,y1),(3))
  x2 = random.randint(0,width)
  y2 = random.randint(0,height)
  distance_from_center = math.hypot(x2 - circle_x, y2 - circle_y) 
  is_in_circle = distance_from_center <= radius
  if is_in_circle:
    score2+=1
    color = BLUE
  else:
    color = YELLOW
  pygame.draw.circle(screen,(color),(x2,y2),(3))
  pygame.display.update()    
while True:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()     
print (Player1)
print (Player2)  
        
  
  

