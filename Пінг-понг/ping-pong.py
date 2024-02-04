from pygame import *

win_width = 700
win_height = 500

speed_x = 3
speed_y = 3

img_truba1 = "Truba1.png"
img_truba2 = "Truba2.png"
img_ball = "boll.png"


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, sixe_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, sixe_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < win_height - 100: 
            self.rect.y += self.speed 
class Player2(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < win_height - 100: 
            self.rect.y += self.speed


display.set_caption("Пінг-Понг")
window = display.set_mode((win_width, win_height))
background = (75, 156, 98)
window.fill(background)

raketka_left = Player1(img_truba1, 50, 350, 70, 100, 5 )
raketka_right = Player2(img_truba1, 570, 50, 70, 100, 5 )
ball = GameSprite(img_ball, 200, 200, 50, 50, 20)

finish = False
clock = time.Clock()
FPS = 60
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill(background)
        raketka_left.update()
        raketka_right.update()
        ball.update()
        raketka_right.reset()
        ball.reset()
        raketka_left.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(img_truba1, ball) or sprite.collide_rect(img_truba2, ball):
        speed_x *= -1
        display.update()

    clock.tick(FPS)