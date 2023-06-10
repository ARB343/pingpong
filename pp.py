from pygame import *
from random import randint
from time import time as timer

score = 0
lost = 0
max_lost = 3
max_score = 10
font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 36)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, playerIm, playerX, playerY, sizex, sizey, playerSpd):
        super().__init__()
        self.image = transform.scale(image.load(playerIm), (sizex, sizey))
        self.speed = playerSpd
        self.rect = self.image.get_rect()
        self.rect.x = playerX
        self.rect.y = playerY
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 410:
            self.rect.y += self.speed
 



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_y:
            self.rect.x = randint(80, win_x - 80)
            self.rect.y = 0
            lost = lost + 1
            mixer.Sound('hrenas-dva.ogg').play()

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


win_x = 700
win_y = 500
window = display.set_mode((win_x, win_y))
display.set_caption('Не Лабиринт')
bkg = transform.scale(image.load('dom.jpg'), (win_x, win_y))

rel_time = False
time_fire = True
game = True
finish = False
FPS = 24
clock = time.Clock()
life = 3
font.init()
font = font.Font(None, 70)

ship = Player('treasure.png', 5, win_y - 100, 80, 100, 10 )


mixer.init()


while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        window.blit(bkg, (0, 0))
        
        ship.update()
        
        ship.reset()
   
    display.update()
    clock.tick(30)