from pygame import *
from random import randint

win_width = 700
win_height = 500

font.init()
font2 = font.Font(None, 36)
font1 = font.Font(None, 80)
win = font1.render("YOU WIN", True, (255, 255, 255))
lose = font1.render("YOU LOSE", True, (180, 0, 0))


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


class Player(GameSprite):
    def right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y += self.rect.y
        if keys [K_d] and self.rect.x < win_height - 80:
            self.rect.y -= self.rect.y

    def left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y += self.rect.y
        if keys [K_s] and self.rect.y < win_height - 80:
            self.rect.y -= self.rect.y

display.set_caption("Пінг-Понг")
window = display.set_mode((win_width, win_height))
background = (75, 156, 98)
window.fill(background)

finish = False

run = True
while run:

    display.update()

    time.delay(50)