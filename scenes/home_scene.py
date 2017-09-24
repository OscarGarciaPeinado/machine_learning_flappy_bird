import pygame
from pygame.constants import KEYDOWN, K_SPACE, K_KP_ENTER

from config import WIDTH, HEIGHT
from entities.floor import Floor
from entities.menu import Menu
from scenes.play_scene import PlayScene
from scenes.scene import Scene
from utils import root_path, get_repeated_surface


class HomeScene(Scene):
    def __init__(self, game):
        Scene.__init__(self, game)
        self.initialize_bg(game.screen)
        self.initialize_menu()

    def initialize_bg(self, screen):
        self.floor = Floor()
        screen.fill((0, 153, 204))
        # get_repeated_surface(pygame.image.load(root_path + '/assets/buildings.png'), WIDTH)

    def initialize_menu(self):
        self.menu = Menu(WIDTH)

    def on_update(self):
        self.floor.next()
        self.menu.next()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.game.change_scene(PlayScene(self.game))

    def on_draw(self, screen):
        screen.blit(self.floor.image, (self.floor.x, self.floor.y))
        screen.blit(self.menu, self.menu.get_rect())
