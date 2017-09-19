import pygame

from config import HEIGHT
from utils import root_path


class Menu(pygame.Surface):
    orange = (219, 200, 54)
    menu_options = ["START"]

    def __init__(self, width):
        pygame.Surface.__init__(self, (width, HEIGHT), pygame.SRCALPHA, 32)
        self.convert_alpha()
        self.select_option = "START"
        self.set_header((width / 2))

    def set_header(self, center_x):
        font = pygame.font.Font(root_path + '/assets/flappy_bird_font.ttf', 80)
        header, header_rect = self.text_objects("Flappy Bird 0 ML", font)
        header_rect.center = (center_x, (HEIGHT / 5))
        self.blit(header, header_rect)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.orange)
        return textSurface, textSurface.get_rect()

    def add_option(self, text):
        pass

    def select_option(self):
        pass
