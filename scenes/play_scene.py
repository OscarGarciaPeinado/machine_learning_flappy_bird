import pygame

from config import WIDTH, HEIGHT, GAME_WIDTH, MAP_SPEED
from entities.bird import Bird
from entities.floor import Floor
from entities.pipes import Pipes
from entities.score import Score
from repository.image_loader import ImageLoader
from scenes.scene import Scene


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
        self.score = Score(GAME_WIDTH, WIDTH - GAME_WIDTH, [self.bird])

    def initialize_pipes(self):
        self.pipes = []
        pipes = Pipes(GAME_WIDTH, HEIGHT, MAP_SPEED)
        self.pipes.append(pipes)

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
        self.check_collision()
        self.refresh_birds_score()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
            self.bird.jump()

    def on_draw(self, screen):
        for pipes in self.pipes:
            pipes.draw(screen)

        screen.blit(self.floor.image, (self.floor.x, self.floor.y))
        if not self.bird.dead:
            screen.blit(self.bird.image, self.bird.rect)
        self.score.draw(screen)

    def refresh_pipes(self):
        if GAME_WIDTH - self.pipes[-1].get_x() > 170:
            pipes = Pipes(GAME_WIDTH, HEIGHT, MAP_SPEED)
            self.pipes.append(pipes)
        for pipes in self.pipes:
            pipes.increase_x()

        self.pipes = [pipes for pipes in self.pipes if pipes.get_x() + pipes.get_width() > 0]

    def check_collision(self):
        for pipes in self.pipes:
            if pipes.is_collision(self.bird.rect):
                self.bird.dead = True

    def refresh_birds_score(self):
        first_not_visited_pipe = next(pipes for pipes in self.pipes if not pipes.visited)
        if not self.bird.dead and first_not_visited_pipe.get_x() + first_not_visited_pipe.get_width() < GAME_WIDTH / 2:
            for pipes in self.pipes:
                if not pipes.visited:
                    pipes.visited = True
                    break
            self.bird.score += 1
