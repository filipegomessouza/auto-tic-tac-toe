import config
from src.game.tic_tac_toe_game import TicTacToeGame
from src.exceptions.players_with_equal_play_option_exception import PlayersWithEqualPlayOptionException
from src.algorithms.genetic_algorithm import GeneticAlgorithm
from src.game.players.neural_network_player import NeuralNetworkPlayer

genetic_algorithm = GeneticAlgorithm()
best_player: NeuralNetworkPlayer = genetic_algorithm.run()
best_player.set_time_to_wait_after_playing_move_in_seconds(config.TIME_TO_WAIT_AFTER_PLAYING_MOVE_IN_SECONDS)

# try:
#     game = TicTacToeGame(
#         config.RANDOM_PLAYER_O,
#         best_player,
#         config.SHOULD_RENDER,
#     )
# except PlayersWithEqualPlayOptionException as e:
#     print(e)
#     exit(1)

# game.run()
