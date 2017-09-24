import pygame
from pygame.locals import *

import math

from repository.image_loader import ImageLoader
from config import WIDTH, HEIGHT, MAP_SPEED
from utils import get_repeated_surface


class Floor(pygame.sprite.Sprite):
    def __init__(self, width=WIDTH):
        pygame.sprite.Sprite.__init__(self)
        self.base = ImageLoader().get_image("base.png")

        self.image = get_repeated_surface(self.base, width)
        self.rect = self.image.get_rect()
        self.x = 0
        self.x_difference = self.image.get_width() - width
        self.y = HEIGHT - self.base.get_height()

    def next(self):
        self.x = -((-self.x + MAP_SPEED) % self.base.get_width())
