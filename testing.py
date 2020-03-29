## Beginner tutorials here ##
import pygame as pg
import random
from Player import Player
from Mob import Mob
from Platform import Platform

# Window size
WIDTH = 1000
HEIGHT = 700

FPS = 30 # Screen will updated at 30 fps

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

jumping = False


pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Platformer")
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
mobs = pg.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(9):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Game Loop
endgame = False
while(endgame == False):
    clock.tick(FPS) # Ensures correct fps

    # Events
    for event in pg.event.get():
        # Check for closing window
        if(event.type == pg.QUIT):
            endgame = True
        if(event.type == pg.KEYDOWN):
            if(event.key == pg.K_ESCAPE):
                endgame = True


    # Update
    all_sprites.update()

    # Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pg.display.flip() # implements display buffer aka double buffering implementation



pg.quit()
