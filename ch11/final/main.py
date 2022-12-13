import pygame
from pygame.locals import*
import math


class Brush():
  def __init__(self):
    pass
  class Painter():
    def __init__(self):
      self.screen =  pygame.display.set_mode((800, 600))
  pygame.display.set_caption("Painter")
  self.clock = pygame.time.Clock()
  def run(self):
      self.screen.fill((255, 255, 255))
while True:
# max fps limit
  self.clock.tick(40)
  for event in pygame.event.get():
    if event.type == QUIT: 
      return
    elif event.type == KEYDOWN:
      pass
    elif event.type == MOUSEBUTTONDOWN:
      pass
    elif event.type == MOUSEMOTION:
      pass
    elif event.type == MOUSEBUTTONUP:
      pass
pygame.display.update()
if __name__ == '__main__':
 app = Painter()

app.run()

class Brush():
  def __init__(self,screen):
    self.screen = screen
    self.color = (0,0,0)
    self.size = 1 
self.drawing = False
def start_draw(self):
  self.drawing = True
def end_draw(self):
  self.drawing = False
def draw(self,pos):
  if self.drawing:
    pygame.draw.circle(self.screen,self.color,pos,self.size)


  class Painter():
    def __init__(self):
      self.screen = pygame.display.set_mode((800, 600))
      pygame.display.set_caption("Painter")
      self.clock = pygame.time.Clock()
      self.brush = Brush(self.screen)
      self.menu = Menu(self.screen)
      self.menu.set_brush(self.brush)
    
    def run(self):
      self.screen.fill((255,255,255))
  if event.key == K_ESCAPE:
    self.screen.fill((255,255,255))
  elif event.type == MOUSEBUTTONDOWN:
    self.brush.start_draw()
  elif event.type == MOUSEMOTION:
    self.brush.draw(event.pos)
  elif event.type == MOUSEBUTTONUP:
    self/brush.end_draw()
    class Brush():
      def __init__(self,screen):
        self.screen = screen
        self.color = (0,0,0)
        self.size = 1 
        self.drawing = False
    def drawing = False
    def start_draw(self):
      self.drawing = True
    def end_draw(self):
      self.drawing = False
    def end_draw(self):
      self.drawing = False
    def draw(self,pos):
      if self.drawing:
        pygame.draw.circle(self.screen,self.color,pos,self.size)
class Painter():
  def__init__(self):
  self.screen = pygame.display.set_mode((800,600))
    pygame.display.set_captiom("Painter")
    self.clock = pygame.time.Clock()
    self.brush = Brush(self.screen)
self.brush = Brush(self.screen)
def run(self):
  self.screen.fill((255,255,255))
while True:
  self.clock.tick(40)
  for eventin pygame.event.get:
  if event.type == QUIT():
    return
    
  elif event.type == KEYDOWN:
    if event.key == K_ESCAPE:
      self.screen.fill((255,255,255))
    elif event.type ==MOUSEBUTTONDOWN:
      self.brush.start_draw()
    elif event.type == MOUSEMOTION: 
      self.brush.draw(event.pos)
    elif event.type == MOUSEBUTTONUP:
      self.brush.end_draw()

class Brush():
  delf.screen = screen
  self.color = (0,0,0)
  self.size = 1 
  self.drawing = False
  self.last_pos = None
def start_draw(self,pos):
  self.drawing = True
  self.last_pos = pos
def end_draw(self) = False
def draw(self,pos):
  if self.drawing:
    pygame.draw.line(se;f.screen,self.color,self.last_pos,pos,self.size*2)
    self.last_pos = Pos

class Brush():
  def __init__(self.screen):
  self.screen = screen
  self.color(0,0,0)
  self.size = 1 
  self.drawing = False
  self.last_pos = None
  self.space = 1 
  self.style = False
self.brush = pygame.image.load("brush.png").convert_alpa()
self.brush_now = self.brush.subsurface((0,0),(1,1))
def start_draw(self,pos):
  self.drawing = True
self.last_pos = pos 
def end_draw(self):
  self.drawing = False  
  def set_brush_style(self,style):
    print"*set brush style to",style
    self.style = style
    def get_brush_style(self):
      return self.style
      def set_size(self,size):
         if size <0.5:size = 0.5
              elif size > 50: size = 50
                print"set brudh size to",size 
self.size = size 
self.brush_now = self.brush.subsurface((0,0),(size*2,size*2))
def get_size(self):
  return self.size
def draw(self,pos):
  if self.drawing:
    for p in self._get_points(pos):
      if self.style == False:
        pygame.draw.circle(self.screen,self.colo,p,self.size)
  else:
self.screen.blit(self.brush_now, p)
self.last_pos = pos
def _get_points(self, pos):
  """ Get all points between last_point ~ now_point. """

  
  points = [ (self.last_pos[0], self.last_pos[1]) ]
  len_x = pos[0] - self.last_pos[0]
  len_y = pos[1] - self.last_pos[1]
  length = math.sqrt(len_x ** 2 + len_y ** 2)
  step_x = len_x / length
  step_y = len_y / length
  for i in xrange(int(length)):
  points.append(
  (points[-1][0] + step_x, points[-1][1] + step_y))
  points = map(lambda x:(int(0.5+x[0]), int(0.5+x[1])), points)

return list(set(points))

class Menu():
  def __init__(self, screen):
  self.screen = screen
  self.brush = None
self.clock.tick(30)
for event in pygame.event.get():
  if event.type == QUIT:
    return
  elif event.type == KEYDOWN:

  if event.key == K_ESCAPE:
      self.screen.fill((255, 255, 255))
  elif event.type == MOUSEBUTTONDOWN:

  if ((event.pos)[0] <= 74 and
self.menu.click_button(event.pos)):

  pass
  else:
    self.brush.start_draw(event.pos)
    elif event.type == MOUSEMOTION:
      self.brush.draw(event.pos)
      elif event.type == MOUSEBUTTONUP:
        self.brush.end_draw()
          self.menu.draw()
          pygame.display.update()
            if __name__ == '__main__':
            app = Painter()
                app.run()


