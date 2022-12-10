import pygame
import sys

pygame.init()

gameover_font = pygame.font.Font("font/font.ttf",48)
again_image = pygame.image.load("images/again.png").convert_alpha()
gameover_image = pygame.image.load("images/gameover.png").convert_alpha()

wrong_matches = []

if match_NUM > 0:
  for each in wrong_matches:
    if each.active ==True:
      each.move()
      screem.blit(each.image,each.rect)
    
pygame.mixer.music.stop()

gameover_socre = gameover_font.render("Score : %s" % str(score), True, Whitefont())
screen.blit(gameover_score,(100,200)) 
screen.blit(again_image,(90,350))
screen.blit(gameover_image,(90,450))
mouse_down = pygame.mouse .get_pressed()
if mouse_down[0]:
    pos = pygame.mouse.get_pos()
    if 90 < pos[0] < 390 and 350 < pos[1] < 390:
      main()
    elif 90 < pos[0] < 390 and 450 < pos[1] < 490:
          pygame.quit
          sys.exit()