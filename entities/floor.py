import pygame
from pygame.locals import *

import math

from repository.image_loader import ImageLoader
from config import WIDTH, HEIGHT, MAP_SPEED


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.base = ImageLoader().get_image("base")
        number_of_bases = self.get_base_size()

        self.image = self.get_initial_surface(number_of_bases=number_of_bases)
        self.rect = self.image.get_rect()
        self.x = 0
        self.x_difference = self.image.get_width() - WIDTH
        self.y = HEIGHT - self.base.get_height()

    def get_initial_surface(self, number_of_bases):
        cropped = pygame.Surface((self.base.get_width() * number_of_bases, self.base.get_height()), pygame.SRCALPHA, 32)
        x = 0
        for base in range(number_of_bases):
            cropped.blit(self.base, (x, 0))
            x += self.base.get_width()
        return cropped

    def get_base_size(self):
        return math.ceil(WIDTH / self.base.get_width()) + 1

    def next(self):
        self.x = -((-self.x + MAP_SPEED) % self.base.get_width())
