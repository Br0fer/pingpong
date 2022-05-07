from pygame import *

img_back = "backgroundpp.jpg"
img_racket = "racket.png"
img_ball = "ball.png"

class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
                
win_width = 600
win_height = 500
display.set_caption("PingPong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

finish = False
game = True
clock = time.Clock()
FPS = 60

racket1 = Player(img_racket, 30, 200, 4, 25, 75)
racket2 = Player(img_racket, 520, 200, 4, 25, 75)
ball = GameSprite(img_ball, 200, 200, 4, 50, 50)

font.init()
font = fontFont(None, 35)
lose1 = font.render("Player1 LOSE!",  True, (180, 0, 0))
lose2 = font.render("Player2 LOSE!",  True, (180, 0, 0))

speed_x = 3
speed_y = 3



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        background = transform.scale(image.load(img_back), (win_width, win_height))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            game = False
            window.blit(lose1, (200, 200))
        if ball.rect.x > 600:
            finish = True
            game = False
            window.blit(lose2, (200, 200))
        racket1.reset()
        racket2.reset()
        ball.reset()
        
    display.update()
    clock.tick(FPS)
            
            
