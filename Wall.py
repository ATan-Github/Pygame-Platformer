## Wall Class ##
import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        # Makes the surface
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 255))

        # Places the platform
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

