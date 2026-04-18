from src.algorithms.algorithm import Algorithm
from src.neural_networks.one_hidden_layer_neural_network import OneHiddenLayerNeuralNetwork
from src.game.board import Board
from src.game.players.neural_network_player import NeuralNetworkPlayer
from src.game.players.random_player import RandomPlayer
from src.game.players.distracted_player import DistractedPlayer
from src.enums.play_option import PlayOption
from src.game.tic_tac_toe_game import TicTacToeGame
from src.game.players.player import Player
import numpy as np

class GeneticAlgorithm(Algorithm):
    POPULATION_SIZE = 100
    MUTATION_RATE = 0.8
    CHANGE_STEP_RATE = 0.9
    ELITE_SIZE = 20
    GAMES_TO_EVAL_INDIVIDUAL = 30
    WIN_POINTS = 3
    DRAW_POINTS = 1
    LOSS_POINTS = 0

    def __init__(self):
        self.__random_player = RandomPlayer('Random', PlayOption.O)
        self.__distracted_player = DistractedPlayer('Distracted', PlayOption.O, 0.9)

        self.__neural_network_player = NeuralNetworkPlayer(
            'AI',
            PlayOption.X,
            OneHiddenLayerNeuralNetwork(Board.BOARD_SIZE, 2 * Board.BOARD_SIZE, Board.BOARD_SIZE)
        )

        self.__tic_tac_toe_game = TicTacToeGame(self.__neural_network_player, self.__random_player, False)


    def run(self) -> Player:
        population = self.initialize_population()

        population = self.run_first_block(population)

        best_individual_index = np.argmax(self.evaluate_population_fitness(population))
        best_individual = population[best_individual_index]
        self.__neural_network_player.set_neural_network(best_individual)

        return self.__neural_network_player


    def run_first_block(self, population: np.ndarray) -> np.ndarray:
        while True:
            fitness_scores = self.evaluate_population_fitness(population)

            elite_scores = self.get_elite_fitness_scores(fitness_scores)

            if np.mean(elite_scores) >= self.CHANGE_STEP_RATE:
                break

            # seleção, crossover e mutação

        return population

    def get_elite_population(self, population: np.ndarray, fitness_scores: np.ndarray) -> np.ndarray:
        elite_indices = np.argsort(fitness_scores)[-self.ELITE_SIZE:]

        return population[elite_indices]

    def get_elite_fitness_scores(self, fitness_scores: np.ndarray) -> np.ndarray:
        elite_indices = np.argsort(fitness_scores)[-self.ELITE_SIZE:]

        return fitness_scores[elite_indices]

    def initialize_population(self) -> np.ndarray:
        return np.array([OneHiddenLayerNeuralNetwork(Board.BOARD_SIZE ** 2, 2 * Board.BOARD_SIZE ** 2, Board.BOARD_SIZE ** 2) for _ in range(self.POPULATION_SIZE)])

    def evaluate_population_fitness(self, population: np.ndarray) -> np.ndarray:
        return np.array([self.evaluate_fitness(individual) for individual in population])

    def evaluate_fitness(self, individual: OneHiddenLayerNeuralNetwork) -> float:
        self.__neural_network_player.set_neural_network(individual)

        fitness = 0

        for _ in range(self.GAMES_TO_EVAL_INDIVIDUAL):
            winner_player = self.__tic_tac_toe_game.run()

            if winner_player is None:
                fitness += self.DRAW_POINTS
            elif winner_player is self.__neural_network_player:
                fitness += self.WIN_POINTS
            else:
                fitness += self.LOSS_POINTS

        return fitness / (self.GAMES_TO_EVAL_INDIVIDUAL * self.WIN_POINTS)

    def select_parents(self, population: np.ndarray, fitness_scores: np.ndarray) -> np.ndarray:
        

        # Code to select parents based on fitness scores
        pass

    def crossover(self, parents: np.ndarray) -> np.ndarray:
        # Code to perform crossover between parents to create offspring
        pass

    def mutate(self, offspring: np.ndarray) -> np.ndarray:
        # Code to apply mutation to the offspring
        pass

    def create_new_population(self, mutated_offspring: np.ndarray) -> np.ndarray:
        # Code to create a new population for the next generation
        pass