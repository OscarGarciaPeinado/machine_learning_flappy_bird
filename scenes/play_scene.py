import pygame

from config import WIDTH, HEIGHT, GAME_WIDTH, MAP_SPEED
from entities.bird import Bird
from entities.floor import Floor
from entities.menu import Menu
from repository.image_loader import ImageLoader
from scenes.scene import Scene
from utils import root_path, get_repeated_surface


class PlayScene(Scene):
    add_pipes = True

    def __init__(self, game):
        Scene.__init__(self, game)
        self.image_loader = ImageLoader()
        self.initialize_bg(game.screen)
        self.initialize_map()
        self.initialize_flappy()
        self.pipes = []
        self.create_pipe()

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
        self.refresh_pipes()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
            self.bird.jump()

    def on_draw(self, screen):
        screen.blit(self.floor.image, (self.floor.x, self.floor.y))
        screen.blit(self.bird.image, (self.bird.x, self.bird.y))
        for lower_pipes in self.pipes:
            screen.blit(lower_pipes["image"], (lower_pipes["x"], lower_pipes["y"]))

    def refresh_pipes(self):
        if GAME_WIDTH - self.pipes[-1]["x"] > 170:
            self.create_pipe()
        for lower_pipes in self.pipes:
            lower_pipes["x"] -= MAP_SPEED

    def create_pipe(self):
        lower_pipe = self.image_loader.get_image("pipe-green.png")
        x = WIDTH + lower_pipe.get_width()
        y = HEIGHT - self.floor.image.get_height() - lower_pipe.get_height()
        self.pipes.append({"image": lower_pipe, "x": x, "y": y})
