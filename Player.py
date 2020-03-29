# Player class
import pygame
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

WIDTH = 1000
HEIGHT = 700


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "smallercoollink.png")).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 700)
        self.speedx = 0
        self.speedy = 0
        self.jumping = False
        self.jumpCount = 3

    def update(self):
        self.speedx = 0
        self.speedy = 0

        # Provides basic movement (up/down/left/right)
        keystate = pygame.key.get_pressed() # returns all keys that are pressed at the moment
        if(keystate[pygame.K_LEFT] or keystate[pygame.K_a]):
            self.speedx = -8
        if(keystate[pygame.K_RIGHT] or keystate[pygame.K_d]):
            self.speedx = 8
        if(self.jumping == False):
            # if(keystate[pygame.K_DOWN] or keystate[pygame.K_s]):
            #     self.speedy = 8
            if (keystate[pygame.K_UP] or keystate[pygame.K_SPACE]):
                self.jumping = True
        else:
            if(self.jumpCount >= -10):
                self.speedy -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.jumping = False

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Creates borders of the game
        if(self.rect.right > WIDTH):
            self.rect.right = WIDTH
        if(self.rect.left < 0):
            self.rect.left = 0
        if(self.rect.top < 0):
            self.rect.top = 0
        if(self.rect.bottom > HEIGHT):
            self.rect.bottom = HEIGHT



