# coding: utf-8
from ml_engine.ga_ann_flappy_engine.perceptron import Perceptron


class GaFlappy:
    def __init__(self, birds):
        self.epoch = 1
        self.mutate_rate = 1

        self.best_score = 0
        self.best_fitness = 0

    def initialize_population(self, birds):
        self.population = []
        for bird in birds:
            population = {"name": bird.name, "perceptron": Perceptron()}
            self.population.append(population)

    def update(self, x, y):
        for population in self.population:
            inputs = (x, y)
            population["perceptron"].predict(inputs)
        pass

    def evolve(self):
        winners = self.select_the_best_population()
        if self.mutate_rate and winners[0]["fitness"] < 0:
            pass
        else:
            self.mutate_rate = 0.2

    def mutate(self):
        pass

    def get_random_unit(self):
        pass

    def select_the_best_population(self):
        pass
