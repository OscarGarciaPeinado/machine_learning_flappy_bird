import pygame
from pygame.locals import *

from config import WIDTH, HEIGHT
from repository.image_loader import ImageLoader


class Bird(pygame.sprite.Sprite):
    def __init__(self, name=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = ImageLoader().get_image("redbird-midflap")
        self.rect = self.image.get_rect()
        self.x = WIDTH / 2 - self.image.get_width()
        self.y = HEIGHT / 2 - self.image.get_height()
        self.name = name

    def jump(self):
        pass
