from src.game.tic_tac_toe_game import TicTacToeGame
from src.exceptions.players_with_equal_play_option_exception import PlayersWithEqualPlayOptionException
import config

try:
    game = TicTacToeGame(
        config.NEURAL_NETWORK_PLAYER_X,
        config.NEURAL_NETWORK_PLAYER_O,
        config.SHOULD_RENDER,
    )
except PlayersWithEqualPlayOptionException as e:
    print(e)
    exit(1)

game.run()
