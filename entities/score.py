import pygame
from pygame.rect import Rect

from config import HEIGHT


class Score(object):
    bg_color = (102, 153, 153)

    def __init__(self, x, width):
        self.bg_x = x
        self.bg_width = width

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, (self.bg_x, 0, self.bg_width, HEIGHT))
