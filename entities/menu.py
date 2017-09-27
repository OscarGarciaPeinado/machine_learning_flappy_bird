import pygame

from config import HEIGHT, WIDTH
from entities.option_menu import OptionMenu
from repository.image_loader import ImageLoader
from utils import root_path


class Menu(pygame.Surface):
    orange = (219, 200, 54)
    white = (255, 255, 255)
    arrow_alpha_increment = 1

    y = 0

    def __init__(self, width):
        pygame.Surface.__init__(self, (width, HEIGHT), pygame.SRCALPHA, 32)
        start = OptionMenu("Manual", x=(WIDTH / 2), y=(HEIGHT / 3))
        self.menu_options = {"Manual": start}
        self.select_option = "Manual"
        self.set_header((width / 2))
        image_loader = ImageLoader()
        self.arrow = image_loader.get_image("arrow.png").convert_alpha()
        self.blit(start, (start.x, start.y))
        self.blit(self.arrow, ((start.x - self.arrow.get_width() - 15), (start.y + (self.arrow.get_height() / 2))),
                  (0, 0, self.arrow.get_width(), self.arrow.get_height()))

        self.arrow.get_rect()

    def set_header(self, center_x):
        font = pygame.font.Font(root_path + '/assets/flappy_bird_font.ttf', 90)
        header, header_rect = self.text_objects("Flappy Bird 0 ML", font, self.orange)
        header_rect.center = (center_x, (HEIGHT / 5))
        self.blit(header, header_rect)

    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def increase_alpha(self):
        if self.arrow.get_alpha() >= 255:
            self.arrow_alpha_increment = -1
        elif self.arrow.get_alpha() <= 30:
            self.arrow_alpha_increment = 1
        self.arrow.set_alpha(self.arrow.get_alpha() + self.arrow_alpha_increment)
        self.arrow.convert()

    def next(self):

        self.increase_alpha()
        option = self.menu_options[self.select_option]
        self.blit(self.arrow,
                  ((option.x - self.arrow.get_width() - 15), (self.y + option.y + (self.arrow.get_height() / 2))),
                  (0, 0, self.arrow.get_width(), self.arrow.get_height()))
