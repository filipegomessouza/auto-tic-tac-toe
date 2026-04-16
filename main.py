from src.enums.play_option import PlayOption
from src.game.players.human_player import HumanPlayer
from src.game.players.optimal_player import OptimalPlayer
from src.game.players.random_player import RandomPlayer
from src.game.tic_tac_toe_game import TicTacToeGame
from src.exceptions.players_with_equal_play_option_exception import PlayersWithEqualPlayOptionException

player_one = RandomPlayer('Computer 1', PlayOption.X)
player_two = RandomPlayer('Computer 2', PlayOption.O)

try:
    game = TicTacToeGame(player_one, player_two)

except PlayersWithEqualPlayOptionException as e:
    print(e)
    exit(1)

game.run()
