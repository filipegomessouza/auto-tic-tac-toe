from src.enums.play_option import PlayOption
from src.game.players.human_player import HumanPlayer
from src.game.players.optimal_player import OptimalPlayer
from src.game.players.random_player import RandomPlayer
from src.game.tic_tac_toe_game import TicTacToeGame
from src.exceptions.players_with_equal_play_option_exception import PlayersWithEqualPlayOptionException
import config

player_one = config.RANDOM_PLAYER_X
player_two = config.RANDOM_PLAYER_O

try:
    game = TicTacToeGame(
        config.RANDOM_PLAYER_X,
        config.RANDOM_PLAYER_O,
        config.SHOULD_RENDER,
    )
except PlayersWithEqualPlayOptionException as e:
    print(e)
    exit(1)

game.run()
