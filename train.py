from src.algorithms.genetic_algorithm import GeneticAlgorithm
from src.game.players.neural_network_player import NeuralNetworkPlayer
from typing import List

g = GeneticAlgorithm()

# f = g.evaluate_fitness(OneHiddenLayerNeuralNetwork(9, 18, 9))

best_player = g.run()

weights = best_player.get_weights()

with open('weights2.txt', 'w') as file:
    list_weights: List[float] = weights.tolist()

    file.write('\n'.join(map(str, list_weights)))
