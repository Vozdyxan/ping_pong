# Online Python - IDE, Editor, Compiler, Interprete
from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_width - 5:
           self.rect.y += self.speed
           
    def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_width - 5:
           self.rect.y += self.speed
font.init()
font1 = font.SysFont('Arial', 70)

lose_l = font1.render('SUB-ZERO WINS', True, (0, 255, 0))
lose_r = font1.render('SCORPION WINS', True, (0, 255, 0))
           
           
win_width = 700
win_height = 500
win = display.set_mode((win_width, win_height))

back_color = (128, 255, 0)
win.fill(back_color)

ball = Player('tenis_ball.png', width/2, height/2, 50, 50, 4)
racket_l = Player('tenis_ball.png', 50, 370, 50, 150, 4)
racket_r = Player('tenis_ball.png', width-50, height/2, 50, 159, 4)

if ball.rect.x < 0:
   win.blit(lose_1, (200, 200))
   game - False

if ball.rect.x < 0:
   win.blit(, (200, 200))
   game - False

speed_x = 3
speed_y = 3

clock = time.clock()
FPS = 60

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
           
    display.update()
    clock.tick(FPS)
