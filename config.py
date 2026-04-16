from src.game.players.optimal_player import OptimalPlayer
from src.game.players.random_player import RandomPlayer
from src.game.players.human_player import HumanPlayer
from src.enums.play_option import PlayOption

TIME_TO_WAIT_AFTER_PLAYING_MOVE_IN_SECONDS = 0.4
SHOULD_RENDER = True

RANDOM_PLAYER_X = RandomPlayer('Random Player X', PlayOption.X, TIME_TO_WAIT_AFTER_PLAYING_MOVE_IN_SECONDS)
RANDOM_PLAYER_O = RandomPlayer('Random Player O', PlayOption.O, TIME_TO_WAIT_AFTER_PLAYING_MOVE_IN_SECONDS)

OPTIMAL_PLAYER_X = OptimalPlayer('Optimal Player X', PlayOption.X, TIME_TO_WAIT_AFTER_PLAYING_MOVE_IN_SECONDS)
OPTIMAL_PLAYER_O = OptimalPlayer('Optimal Player O', PlayOption.O, TIME_TO_WAIT_AFTER_PLAYING_MOVE_IN_SECONDS)

HUMAN_PLAYER_X = HumanPlayer('Human Player X', PlayOption.X)
HUMAN_PLAYER_O = HumanPlayer('Human Player O', PlayOption.O)
