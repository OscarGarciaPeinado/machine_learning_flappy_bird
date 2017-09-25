import pygame

from config import WIDTH, HEIGHT, GAME_WIDTH, MAP_SPEED
from entities.bird import Bird
from entities.floor import Floor
from entities.menu import Menu
from entities.score import Score
from repository.image_loader import ImageLoader
from scenes.scene import Scene
from random import randint
from utils import root_path, get_repeated_surface, rotate_center


class PlayScene(Scene):
    add_pipes = True

    def __init__(self, game):
        Scene.__init__(self, game)
        self.image_loader = ImageLoader()
        self.initialize_bg(game.screen)
        self.initialize_pipes()
        self.initialize_flappy()
        self.initialize_pipes()
        self.initialize_score()

    def initialize_score(self):
        self.score = Score(GAME_WIDTH, WIDTH - GAME_WIDTH)

    def initialize_pipes(self):
        self.pipes = []
        self.create_pipe()

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
        for lower_pipes, upper_pipes in self.pipes:
            screen.blit(lower_pipes["image"], (lower_pipes["x"], lower_pipes["y"]))
            screen.blit(upper_pipes["image"], (upper_pipes["x"], upper_pipes["y"]))

        screen.blit(self.floor.image, (self.floor.x, self.floor.y))
        screen.blit(self.bird.image, (self.bird.x, self.bird.y))
        self.score.draw(screen)

    def refresh_pipes(self):
        if GAME_WIDTH - self.pipes[-1][0]["x"] > 170:
            self.create_pipe()
        for lower_pipes, upper_pipes in self.pipes:
            lower_pipes["x"] -= MAP_SPEED
            upper_pipes["x"] -= MAP_SPEED

    def create_pipe(self):
        lower_pipe = self.image_loader.get_image("pipe-green.png")
        x = GAME_WIDTH + lower_pipe.get_width()
        y = HEIGHT - lower_pipe.get_height()
        y = y + randint(-100, 100)

        upper_pipe, upper_rect = rotate_center(lower_pipe, lower_pipe.get_rect(), 180)
        self.pipes.append(({"image": lower_pipe, "x": x, "y": y},
                           {"image": upper_pipe, "x": x, "y": y - 100 - upper_pipe.get_height()}))
