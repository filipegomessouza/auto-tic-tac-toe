from src.algorithms.algorithm import Algorithm
from src.neural_networks.one_hidden_layer_neural_network import OneHiddenLayerNeuralNetwork
from src.game.board import Board
from src.game.players.neural_network_player import NeuralNetworkPlayer
from src.game.players.random_player import RandomPlayer
from src.game.players.distracted_player import DistractedPlayer
from src.enums.play_option import PlayOption
from src.game.tic_tac_toe_game import TicTacToeGame
from src.game.players.player import Player
from src.utils.debug import dd
import numpy as np
import random
import time

class GeneticAlgorithm(Algorithm):
    POPULATION_SIZE = 100
    MUTATION_RATE = 0.1
    MUTATION_MEAN = 0
    MUTATION_SIGMA = 1
    CHANGE_STEP_RATE = 0.9
    ELITE_SIZE = 5
    GAMES_TO_EVAL_INDIVIDUAL = 30
    WIN_POINTS = 3
    DRAW_POINTS = 1
    LOSS_POINTS = 0
    TOURNAMENT_SIZE = 5
    INITIAL_ERROR_PROBABILITY = 1
    MAX_TIME_IN_SECONDS = 300

    def __init__(self):
        self.__distracted_player = DistractedPlayer('Distracted', PlayOption.O, self.INITIAL_ERROR_PROBABILITY)
        self.__neural_network = OneHiddenLayerNeuralNetwork(Board.BOARD_SIZE ** 2, 2 * Board.BOARD_SIZE ** 2, Board.BOARD_SIZE ** 2)
        self.__neural_network_player = NeuralNetworkPlayer('AI', PlayOption.X, self.__neural_network)
        self.__tic_tac_toe_game = TicTacToeGame(False)

        self.__win_points = self.WIN_POINTS
        self.__draw_points = self.DRAW_POINTS
        self.__loss_points = self.LOSS_POINTS


    def run(self) -> NeuralNetworkPlayer:
        population = self.initialize_population()

        population = self.run_first_block(population)

        best_individual_index = np.argmax(self.evaluate_population_fitness(population))
        best_individual = population[best_individual_index]
        self.__neural_network.set_weights(best_individual)

        return self.__neural_network_player


    def run_first_block(self, population: np.ndarray) -> np.ndarray:
        error_probability = self.INITIAL_ERROR_PROBABILITY

        time_start = time.time()

        while True:
            fitness_scores = self.evaluate_population_fitness(population)
            elite_scores = self.get_elite_fitness_scores(fitness_scores)

            if np.mean(elite_scores) >= self.CHANGE_STEP_RATE:
                error_probability -= 0.1
                print('Decreasing error probability to', error_probability)

                if error_probability <= 0:
                    break

                if error_probability <= 0.4:
                    self.__draw_points = 2

                if error_probability <= 0.2:
                    self.__draw_points = 3
                    self.__loss_points = -10

                self.__distracted_player.set_error_probability(error_probability)

            if time.time() - time_start > self.MAX_TIME_IN_SECONDS:
                print('Max time reached, stopping algorithm')
                break

            next_population = []
            for _ in range(self.ELITE_SIZE, self.POPULATION_SIZE):
                parent1 = self.select_parent(population, fitness_scores)
                parent2 = self.select_parent(population, fitness_scores)

                child = self.crossover(parent1, parent2)
                mutated_child = self.mutate(child)

                next_population.append(mutated_child)


            next_population = np.array(next_population)
            elite_population = self.get_elite_population(population, fitness_scores)

            population = np.concatenate([elite_population, next_population])

        return population

    def get_elite_population(self, population: np.ndarray, fitness_scores: np.ndarray) -> np.ndarray:
        elite_indices = np.argsort(fitness_scores)[-self.ELITE_SIZE:]

        return population[elite_indices]

    def get_elite_fitness_scores(self, fitness_scores: np.ndarray) -> np.ndarray:
        elite_indices = np.argsort(fitness_scores)[-self.ELITE_SIZE:]

        return fitness_scores[elite_indices]

    def initialize_population(self) -> np.ndarray:
        return np.array([self.initialize_individual() for _ in range(self.POPULATION_SIZE)])

    def initialize_individual(self) -> np.ndarray:
        input_size = Board.BOARD_SIZE ** 2
        hidden_size = 2 * input_size
        output_size = input_size

        return np.concatenate([
            np.random.randn(input_size * hidden_size) * 0.5,
            np.zeros(hidden_size),
            np.random.randn(hidden_size * output_size) * 0.5,
            np.zeros(output_size),
        ])

    def evaluate_population_fitness(self, population: np.ndarray) -> np.ndarray:
        return np.array([self.evaluate_fitness(individual) for individual in population])

    def evaluate_fitness(self, individual: np.ndarray) -> float:
        self.__neural_network.set_weights(individual)

        fitness = 0

        player_one = self.__neural_network_player
        player_two = self.__distracted_player

        for _ in range(self.GAMES_TO_EVAL_INDIVIDUAL):
            winner_player = self.__tic_tac_toe_game.run(player_one, player_two)

            if winner_player is None:
                fitness += self.__draw_points
            elif winner_player is self.__neural_network_player:
                fitness += self.__win_points
            else:
                fitness += self.__loss_points

            player_one, player_two = player_two, player_one

        return fitness / (self.GAMES_TO_EVAL_INDIVIDUAL * self.__win_points)

    def select_parent(self, population: np.ndarray, fitness_scores: np.ndarray) -> np.ndarray:
        candidate_indices = np.random.choice(len(population), size=self.TOURNAMENT_SIZE, replace = True)
        best_idx = candidate_indices[np.argmax(fitness_scores[candidate_indices])]

        return population[best_idx]

    def crossover(self, parent1: np.ndarray, parent2: np.ndarray) -> np.ndarray:
        mask = np.random.rand(len(parent1)) < 0.5

        return np.where(mask, parent1, parent2)

    def mutate(self, individual: np.ndarray) -> np.ndarray:
        mask = np.random.rand(len(individual)) < self.MUTATION_RATE
        individual[mask] += np.random.normal(self.MUTATION_MEAN, self.MUTATION_SIGMA, mask.sum())

        return individual
