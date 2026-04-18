import config
from src.enums.play_option import PlayOption
from src.neural_networks.one_hidden_layer_neural_network import OneHiddenLayerNeuralNetwork
from src.game.tic_tac_toe_game import TicTacToeGame
from src.exceptions.players_with_equal_play_option_exception import PlayersWithEqualPlayOptionException
from src.algorithms.genetic_algorithm import GeneticAlgorithm
from src.game.players.neural_network_player import NeuralNetworkPlayer
import numpy as np

with open('weights.txt', 'r') as file:
    weights =  np.array([float(line.strip()) for line in file.readlines()])

neural_network = OneHiddenLayerNeuralNetwork(9, 18, 9)
neural_network.set_weights(weights)

best_player = NeuralNetworkPlayer('AI', PlayOption.X, neural_network, config.TIME_TO_WAIT_AFTER_PLAYING_MOVE_IN_SECONDS)

try:
    game = TicTacToeGame(config.SHOULD_RENDER)
except PlayersWithEqualPlayOptionException as e:
    print(e)
    exit(1)

game.run(
    best_player,
    config.TABLE_PLAYER_O,
)
