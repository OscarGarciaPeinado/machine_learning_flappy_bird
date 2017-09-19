import pygame

from config import WIDTH, HEIGHT
from entities.floor import Floor
from entities.menu import Menu
from scenes.scene import Scene
from utils import root_path, get_repeated_surface


class SceneHome(Scene):
    def __init__(self, game):
        Scene.__init__(self, game)
        self.initialize_bg(game.screen)
        self.initialize_menu()

    def initialize_bg(self, screen):
        self.floor = Floor()
        screen.fill((0, 153, 204))
        get_repeated_surface(pygame.image.load(root_path + '/assets/buildings.png'), WIDTH)

    def initialize_menu(self):
        self.menu = Menu(WIDTH)

    def on_update(self):
        self.floor.next()
        pass

    def on_event(self):
        pass

    def on_draw(self, screen):
        screen.blit(self.floor.image, (self.floor.x, self.floor.y))
        screen.blit(self.menu, self.menu.get_rect())
