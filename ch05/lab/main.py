import pygame
#import initalize 
pygame.init()
def seq3np1(n):
  count = 0
  while(n !=1):

    if(n%2)==0:
      n=n // 2
      count +=1
    else:
      n = n * 3 + 1
      count +=1
  return count

upper_limit= 20
iters= {}

for i in range(2, upper_limit):
   count = seq3np1(i)
   iters[i] = count
print (iters)
width = 400
height = 400
screen = pygame.display.set_mode((width,height)) 

graph = pygame.Surface((width,height))
pygame.font.get_init()
old_x = None
old_y = None
max_val = 0 
max_so_far = 0
graph.fill('white')
scale = 10
textFont = pygame.font.SysFont('arial',20)
for i in range(2, upper_limit):
  x = i
  y = iters[i]
  if y > max_so_far:
    max_val = x
    max_so_far = y
  x = x*scale
  y = y*scale
  if old_x:
    pygame.draw.line(graph,'black',(old_x,old_y),(x,y))
  new_graph = pygame.transform.flip(graph,False, True)
  text = textFont.render("Max so far:"+str(max_so_far),False,'Black')
  screen.blit(new_graph,(0,0))
  screen.blit(text,(0,0))                          
  pygame.display.flip()
  old_x = x
  old_y = y
  
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False
pygame.time.wait(500)

  