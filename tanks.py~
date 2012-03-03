import pygame
from pygame.locals import *
from sys import exit
import os, sys, random
pygame.init()

def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

class figure(pygame.sprite.Sprite):
  def __init__(self, x, y, i_u, i_d, i_l, i_r):
    pygame.sprite.Sprite.__init__(self)
    sprites.add(self)
    self.x = x
    self.y = y
    self.i_u = i_u
    self.i_d = i_d
    self.i_l = i_l
    self.i_r = i_r
    self.image = load_image(self.i_u)
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)
    self.direc = 'u'
    self.move_time = 0
  def move(self, dx, dy):
    if self.move_time < pygame.time.get_ticks():
      self.rect.x += dx
      self.rect.y += dy
      for wall in walls:
	if self.rect.colliderect(wall.rect):
	  if dx > 0:
	    self.rect.right = wall.rect.left
	  if dx < 0:
	    self.rect.left = wall.rect.right
	  if dy > 0:
	    self.rect.bottom = wall.rect.top
	  if dy < 0:
	    self.rect.top = wall.rect.bottom
  def rotateL(self):
    one = 0
    if self.move_time < pygame.time.get_ticks():
      if self.direc == 'u' and one == 0:
	self.direc = 'l'
	self.image = load_image(self.i_l)
	one = 1
      if self.direc == 'l' and one == 0:
	self.direc = 'd'
	self.image = load_image(self.i_d)
	one = 1
      if self.direc == 'd'and one == 0:
	self.direc = 'r'
	self.image = load_image(self.i_r)
	one = 1
      if self.direc == 'r'and one == 0:
	self.direc = 'u'
	self.image = load_image(self.i_u)
	one = 1
  def rotateR(self):
    one = 0
    if self.move_time < pygame.time.get_ticks():
      if self.direc == 'u' and one == 0:
	self.direc = 'r'
	self.image = load_image(self.i_r)
	one = 1
      if self.direc == 'r' and one == 0:
	self.direc = 'd'
	self.image = load_image(self.i_d)
	one = 1
      if self.direc == 'd' and one == 0:
	self.direc = 'l'
	self.image = load_image(self.i_l)
	one = 1
      if self.direc == 'l' and one == 0:
	self.direc = 'u'
	self.image = load_image(self.i_u)
	one = 1
  def shot(self, start):
    self.move_time = pygame.time.get_ticks() + 5000
    self.image = load_image(self.i_u)
    self.direc = 'u'
    self.rect = self.image.get_rect()
    self.rect.center = (start.x, start.y)

class bullet(pygame.sprite.Sprite):
  def __init__(self, x, y, figure, bullets):
    pygame.sprite.Sprite.__init__(self)
    sprites.add(self)
    bullets.add(self)
    self.x = x
    self.y = y
    self.image = pygame.Surface((3, 3))
    self.image.fill((250, 250, 250))
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)
    self.shooting = False
    if figure.direc == 'u':
      self.direc = 'u'
    if figure.direc == 'd':
      self.direc = 'd'
    if figure.direc == 'l':
      self.direc = 'l'
    if figure.direc == 'r':
      self.direc = 'r'
  def move(self, dx, dy, width, height):
    self.rect.x += dx
    self.rect.y += dy
    if self.rect.y < 0:
      self.rect.y = height - 20
    if self.rect.y > height - 20:
      self.rect.y = 0
    if self.rect.x > width:
      self.rect.x = 0
    if self.rect.x < 0:
      self.rect.x = width
    if pygame.sprite.spritecollide(self, walls, False):
      self.kill()
  def update(self, figure):
      if self.direc == 'u':
	self.move(0, -4, width, height)
      if self.direc == 'd':
	self.move(0, 4, width, height)
      if self.direc == 'l':
	self.move(-4, 0, width, height)
      if self.direc == 'r':
	self.move(4, 0, width, height)

class wall(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    walls.add(self)
    sprites.add(self)
    self.x = x
    self.y = y
    self.image = pygame.Surface((10, 10))
    self.image.fill((212, 212, 212))
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)

class start_point(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.x = x
    self.y = y
    self.image = pygame.Surface((10, 10))
    self.image.fill((0, 0, 0))
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)

class flag(pygame.sprite.Sprite):
  def __init__(self, x, y, pic):
    pygame.sprite.Sprite.__init__(self)
    sprites.add(self)
    self.x = x
    self.y = y
    self.pic = pic
    self.image = load_image(self.pic, -1)
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)
  def capture(self, figure, flag):
    if self.rect.colliderect(figure.rect):
      self.rect = figure.rect
      self.rect.center = figure.rect.center
      if self.rect.colliderect(flag.rect):
	if flag == l.flag1:
	  team1.score += 1
	  print team1.score
	  print 'team1 wins!'
	if flag == l.flag2:
	  team2.score += 1
	  print team2.score
	  print 'team2 wins!'
	pygame.time.wait(1000)
	bullets1.empty()
	bullets2.empty()
	bullets3.empty()
	bullets4.empty()
	team1.empty()
	team2.empty()
	starts.empty()
	walls.empty()
	sprites.empty()
	l.new_level = True

class teams(pygame.sprite.RenderUpdates):
  def __init__(self, name):
    pygame.sprite.RenderUpdates.__init__(self)
    self.name = name
    self.score = 0

class score(pygame.sprite.Sprite):
  def __init__(self, team, x, y):
    pygame.sprite.Sprite.__init__(self)
    sprites.add(self)
    self.team = team
    self.score= team.score
    self.font = pygame.font.Font(None, 20)
    if self.team == team1:
      self.text = "Team1: %i" % (self.score)
    if self.team == team2:
      self.text = "Team2: %i" % (self.score)
    self.image = self.font.render(self.text, False, (255, 255, 255))
    self.rect = x, y
  def update(self):
    if self.team == team1:
      self.image = self.font.render("TEAM1: %i" % (self.score), False, (255, 255, 255))
    if self.team == team2:
      self.image = self.font.render("TEAM2: %i" % (self.score), False, (255, 255, 255))


def create_player(figure, move, shoot, speed, bullets):
  key = pygame.key.get_pressed()
  if key[move]:
    if figure.direc == 'u':
      figure.move(0, -speed)
      if figure.rect.y <= 0:
	figure.rect.y = height - 20
    if figure.direc == 'r':
      figure.move(speed, 0)
      if figure.rect.x >= width:
	figure.rect.x = 0
    if figure.direc == 'd':
      figure.move(0, speed)
      if figure.rect.y >= height - 20:
	figure.rect.y = 0   
    if figure.direc == 'l':
      figure.move(-speed, 0)
      if figure.rect.x <= 0:
	figure.rect.x = width
  if key[shoot] and figure.alive() and figure.move_time < pygame.time.get_ticks():
    if len(bullets) < 1:
      b = bullet(figure.rect.x + 4, figure.rect.y + 4, figure, bullets)
def rotate_player(figure, left, right):
    if event.key == left:
      figure.rotateL()
    if event.key == right:
      figure.rotateR()

#creates screeen#
width = 350
height = 320 
depth = 0
fullscreen = 0
screen = pygame.display.set_mode((width, height), fullscreen , depth) 
clock = pygame.time.Clock()

running = True

bullets1 = pygame.sprite.RenderUpdates()
bullets2 = pygame.sprite.RenderUpdates()
bullets3 = pygame.sprite.RenderUpdates()
bullets4 = pygame.sprite.RenderUpdates()
team1 = teams('team1')
team2 = teams('team2')
starts = pygame.sprite.RenderUpdates()
walls = pygame.sprite.RenderUpdates()
sprites = pygame.sprite.RenderUpdates()
class game():
  def __init__(self):
    self.new_level = True
  def create(self):
    if self.new_level:
      level = [
      "WWWWWWWWW     WWWWWWW     WWWWWWWWW",
      "WRR RR RR        RRR      RRRR RRRW",
      "WR f  1 R    RWWWWRRWWWWR  RR 3 RRW",
      "WRR RR RRR      RRRR      R RR RRRW",
      "WRR  WWWWW   RRR      RRRWWWWWRRRRW",
      "WRR  W   R  R    R     RW     RRRRW",
      "WRRRRW RR RRRWWWWRWWWWWRWRR     RRW",
      "WRR    R  RRR    R     RRRR    RRRW",
      "WRRRWWRRWWRR    RR   R   RR     RRW",
      "WRRR        RWRR  RR     W  R   RRW",
      "WRR     R  RRWRRRWRRR   RW    RRRRW",
      "WRWRWRR RRWWWWRRRWRRRR   W R RRRRRW",
      "WRRR W R  RR  RRRWRRR   RR      RRW",
      " RRRR    RR  RR   RRRRWWWWWRR   RR ",
      "     W RR   RR sS  RRRR      RRRRR ",
      "     W RRR   RR  tT RRRR      RRRR ",
      " RRR   RR   RRRR R RR          RRR ",
      "WRRRWWWRRWWWWRR    RR       RRRRRRW",
      "WRRR   RRR   RRR         RR R   RRW",
      "W   RR  RRWRR     RRRWWWRWWWRRRRRRW",
      "WRRR   RRRWRRRR     R  RR    RRRRRW",
      "W R   R RR   RRR     RR RRWWWWWWRRW",
      "W R    RRRWWWWRRWWWWWRRRRR    RRRRW",
      "W R   RRRR   RR      R  RRWR    RRW",
      "WR R  R RRRWWWRR  RRWRRRRRWRRR  RRW",
      "WR RWWR  RR   R  RRRWR  RRWRR  RRRW",
      "WRRR  RRWW   RR        RRRRR RR RRW",
      "WRR 2 RRRRRWWWWWWRR      RR 4  F RW",
      "WRRR RRRR      RRRRRR        RR RRW",
      "WWWWWWWWW     WWWWWWW     WWWWWWWWW",
      ]
      x = y = 5
      for row in level:
	for col in row:
	  if col == "1":
	    self.f_1 = figure(x, y, '/home/david/Programming/Python/tank_game/B_u.jpg', '/home/david/Programming/Python/tank_game/B_d.jpg', '/home/david/Programming/Python/tank_game/B_l.jpg', '/home/david/Programming/Python/tank_game/B_r.jpg')
	  if col == "2":
	    self.f_2 = figure(x, y, '/home/david/Programming/Python/tank_game/B_u.jpg', '/home/david/Programming/Python/tank_game/B_d.jpg', '/home/david/Programming/Python/tank_game/B_l.jpg', '/home/david/Programming/Python/tank_game/B_r.jpg')
	  if col == "3":
	    self.f_3 = figure(x, y, '/home/david/Programming/Python/tank_game/G_u.jpg', '/home/david/Programming/Python/tank_game/G_d.jpg', '/home/david/Programming/Python/tank_game/G_l.jpg', '/home/david/Programming/Python/tank_game/G_r.jpg')
	  if col == "4":
	    self.f_4 = figure(x, y, '/home/david/Programming/Python/tank_game/G_u.jpg', '/home/david/Programming/Python/tank_game/G_d.jpg', '/home/david/Programming/Python/tank_game/G_l.jpg', '/home/david/Programming/Python/tank_game/G_r.jpg')
	  if col == "W":
	    wall(x,y)
	  if col == "R":
	    r = random.choice('n' 'n' 'n' 'n' 'n' 'n' ' n' 'n' 'n' 'W')
	    if r == 'W':
	      wall(x,y)
	  if col == "f":
	    self.flag1 = flag(x, y, '/home/david/Programming/Python/tank_game/B_f.jpg')
	  if col == "F":
	    self.flag2 = flag(x, y, '/home/david/Programming/Python/tank_game/G_f.jpg')
	  if col == "s":
	    self.start1 = start_point(x, y)
	  if col == "S":
	    self.start2 = start_point(x, y)
	  if col == "t":
	    self.start3 = start_point(x, y)
	  if col == "T":
	    self.start4 = start_point(x, y)
	  x += 10
	y += 10
	x = 5
      team1.add(self.f_1, self.f_2)
      s1 = score(team1, 40, 304)
      team2.add(self.f_3, self.f_4)
      s2 = score(team2, 260, 304)
      self.new_level = False
l = game()
while running:
  screen.fill((0, 0, 0))
  clock.tick(30)
  l.create()
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
	running = False
      if event.key == K_f:
	 full = pygame.FULLSCREEN
	 screen = pygame.display.set_mode((width, height), full , depth)
      rotate_player(l.f_1, K_a, K_d)
      rotate_player(l.f_2, K_g, K_j)
      rotate_player(l.f_3, K_k, K_SEMICOLON)
      rotate_player(l.f_4, K_LEFT, K_RIGHT)
  create_player(l.f_1, pygame.K_w, K_s, 2, bullets1)
  create_player(l.f_2, pygame.K_y, K_h, 2, bullets2)
  create_player(l.f_3, pygame.K_o, K_l, 2, bullets3)
  create_player(l.f_4, pygame.K_UP, K_DOWN, 2, bullets4)
  bullets1.update(l.f_1)
  bullets2.update(l.f_2)
  bullets3.update(l.f_3)
  bullets4.update(l.f_4)
  if pygame.sprite.spritecollide(l.f_1, bullets3 or bullets4, True):
    l.f_1.shot(l.start1)
  if pygame.sprite.spritecollide(l.f_2, bullets3 or bullets4, True):
    l.f_2.shot(l.start2)
  if pygame.sprite.spritecollide(l.f_3, bullets1 or bullets2, True):
    l.f_3.shot(l.start3)
  if pygame.sprite.spritecollide(l.f_4, bullets1 or bullets2, True):
    l.f_4.shot(l.start4)
  for player in team1:
    l.flag2.capture(player, l.flag1)
  for player in team2:
    l.flag1.capture(player, l.flag2)

  rect_list = sprites.draw(screen)
  pygame.display.update(rect_list)
exit()