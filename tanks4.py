import pygame
from pygame.locals import *
from sys import exit
import os, sys
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
  def move(self, dx, dy):
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
    if self.rect.y <= 0:
      self.rect.y = height
    if self.rect.y >= height:
      self.rect.y = 0
    if self.rect.x >= width:
      self.rect.x = 0
    if self.rect.x <= 0:
      self.rect.x = width
    if pygame.sprite.spritecollide(self, walls, False):
      self.kill()
  def update(self, figure):
      if self.direc == 'u':
	self.move(0, -3, width, height)
      if self.direc == 'd':
	self.move(0, 3, width, height)
      if self.direc == 'l':
	self.move(-3, 0, width, height)
      if self.direc == 'r':
	self.move(3, 0, width, height)

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

def create_player(figure, move, shoot, speed, bullets):
  key = pygame.key.get_pressed()
  if key[move]:
    if figure.direc == 'u':
      figure.move(0, -speed)
      if figure.rect.y <= 0:
	figure.rect.y = height
    if figure.direc == 'r':
      figure.move(speed, 0)
      if figure.rect.x >= width:
	figure.rect.x = 0
    if figure.direc == 'd':
      figure.move(0, speed)
      if figure.rect.y >= height:
	figure.rect.y = 0   
    if figure.direc == 'l':
      figure.move(-speed, 0)
      if figure.rect.x <= 0:
	figure.rect.x = width
  if key[shoot]:
    if len(bullets) < 1:
      b = bullet(figure.rect.x + 4, figure.rect.y + 4, figure, bullets)
def rotate_player(figure, left, right):
    if event.key == left:
      figure.rotateL()
    if event.key == right:
      figure.rotateR()

#creates screeen#
width = 350
height = 300 
depth = 0
fullscreen = 0
screen = pygame.display.set_mode((width, height), fullscreen , depth) 
clock = pygame.time.Clock()

running = True

bullets1 = pygame.sprite.RenderUpdates()
bullets2 = pygame.sprite.RenderUpdates()
bullets3 = pygame.sprite.RenderUpdates()
bullets4 = pygame.sprite.RenderUpdates()
walls = pygame.sprite.RenderUpdates()
sprites = pygame.sprite.RenderUpdates()
f_1 = figure(width * .15, height * .15, 'R_u.jpg', 'R_d.jpg', 'R_l.jpg', 'R_r.jpg')
f_2 = figure(width * .85, height * .15, 'Y_u.jpg', 'Y_d.jpg', 'Y_l.jpg', 'Y_r.jpg')
f_3 = figure(width * .15, height * .85, 'B_u.jpg', 'B_d.jpg', 'B_l.jpg', 'B_r.jpg')
f_4 = figure(width * .85, height * .85, 'G_u.jpg', 'G_d.jpg', 'G_l.jpg', 'G_r.jpg')

level = [
"WWWWWWWWWWWWW      WWWWWWW   WWWWWWW",
"W                    W             W",
"W     WWWWW             WWWWW      W",
"W    W               W             W",
"W   W                W             W",
"W           W              WW      W",
"W           W               W      W",
"W           WWWWWWWW          W    W",
"W                           WW     W",
"W        W            W     W      W",
"W        W            W            W",
"W        W                         W",
"                                    ",
"             WWWWWW                 ",
"W       W                 WWWWW    W",
"W       W   WWW           W        W",
"W       W                   W      W",
"W       W         Wwwwwww  W       W",
"W       W         W         W      W",
"W       W        W          W       ",
"        W       W                   ",
"        W                   W       ",
"   W        WWWWWWWW         W      ",
"   W                     WWWW       ",
"   W                     W          ",
"W  W        WWWW         W          ",
"W  W                     W         W",
"W  W                     W         W",
"W          WWWWWWWW                W",
"W                                  W",
"WWWWWWWWWWWWW      WWWWWWW   WWWWWWW",
]
x = y = 0
for row in level:
  for col in row:
    if col == "W":
      wall(x,y)
    x += 10
  y += 10
  x = 0

while running:
  screen.fill((0, 0, 0))
  clock.tick(30)
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
	running = False
      if event.key == K_f:
	 full = pygame.FULLSCREEN
	 screen = pygame.display.set_mode((width, height), full , depth)
      rotate_player(f_1, K_a, K_d)
      rotate_player(f_2, K_j, K_l)
      rotate_player(f_3, K_v, K_n)
      rotate_player(f_4, K_LEFT, K_RIGHT)
  create_player(f_1, pygame.K_w, K_s, 2, bullets1)
  create_player(f_2, pygame.K_i, K_k, 2, bullets2)
  create_player(f_3, pygame.K_b, K_SPACE, 2, bullets3)
  create_player(f_4, pygame.K_UP, K_DOWN, 2, bullets4)
  bullets1.update(f_1)
  bullets2.update(f_2)
  bullets3.update(f_3)
  bullets4.update(f_4)
  if pygame.sprite.spritecollide(f_1, bullets2 or bullets3 or bullets4, True):
    f_1.kill()
  if pygame.sprite.spritecollide(f_2, bullets1 or bullets3 or bullets4, True):
    f_2.kill()
  if pygame.sprite.spritecollide(f_3, bullets1 or bullets2 or bullets4, True):
    f_3.kill()
  if pygame.sprite.spritecollide(f_4, bullets1 or bullets2 or bullets3, True):
    f_4.kill()
  rect_list = sprites.draw(screen)
  pygame.display.update(rect_list)
exit()