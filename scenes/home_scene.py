import pygame

from config import WIDTH, MAP_SPEED
from entities.floor import Floor
from entities.menu import Menu
from ml_engine.manual_flappy_engine import ManualFlappyEngine
from scenes.play_scene import PlayScene
from scenes.scene import Scene


class HomeScene(Scene):
    def __init__(self, game):
        Scene.__init__(self, game)
        self.initialize_bg(game.screen)
        self.initialize_menu()

    def initialize_bg(self, screen):
        self.floor = Floor(MAP_SPEED)
        screen.fill((0, 153, 204))

    def initialize_menu(self):
        self.menu = Menu(WIDTH)

    def on_update(self):
        self.floor.refresh()
        self.menu.next()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.game.change_scene(PlayScene(self.game, ManualFlappyEngine()))

    def on_draw(self, screen):
        screen.blit(self.floor.image, self.floor.rect)
        screen.blit(self.menu, self.menu.get_rect())
