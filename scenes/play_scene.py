import pygame

from config import WIDTH, HEIGHT, GAME_WIDTH
from entities.bird import Bird
from entities.floor import Floor
from entities.menu import Menu
from scenes.scene import Scene
from utils import root_path, get_repeated_surface


class PlayScene(Scene):
    def __init__(self, game):
        Scene.__init__(self, game)
        self.initialize_bg(game.screen)
        self.initialize_map()
        self.initialize_flappy()

    def initialize_map(self):
        pass

    def initialize_flappy(self):
        self.bird = Bird(base_y=HEIGHT - self.floor.image.get_height(), name="1")

    def initialize_bg(self, screen):
        self.floor = Floor(GAME_WIDTH)
        screen.fill((0, 153, 204))

    def on_update(self):
        self.game.screen.fill((0, 153, 204))
        self.floor.next()
        self.bird.refresh()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
            self.bird.jump()

    def on_draw(self, screen):
        screen.blit(self.floor.image, (self.floor.x, self.floor.y))
        screen.blit(self.bird.image, (self.bird.x, self.bird.y))
