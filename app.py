import pygame
from scenes.game import Game
from scenes.home_scene import SceneHome

if __name__ == "__main__":
    pygame.init()
    game = Game()
    home_scene = SceneHome(game)
    game.change_scene(home_scene)
    game.loop()
