from src.game.players.optimal_player import OptimalPlayer
from src.game.players.random_player import RandomPlayer
from src.game.players.human_player import HumanPlayer
from src.game.players.distracted_player import DistractedPlayer
from src.enums.play_option import PlayOption

SHOULD_RENDER = True

TIME_TO_WAIT_AFTER_PLAYING_MOVE_IN_SECONDS = 2
ERROR_PROBABILITY_FOR_DISTRACTED_PLAYER = 0.7

RANDOM_PLAYER_X = RandomPlayer('Random Player X', PlayOption.X, TIME_TO_WAIT_AFTER_PLAYING_MOVE_IN_SECONDS)
RANDOM_PLAYER_O = RandomPlayer('Random Player O', PlayOption.O, TIME_TO_WAIT_AFTER_PLAYING_MOVE_IN_SECONDS)

OPTIMAL_PLAYER_X = OptimalPlayer('Optimal Player X', PlayOption.X, TIME_TO_WAIT_AFTER_PLAYING_MOVE_IN_SECONDS)
OPTIMAL_PLAYER_O = OptimalPlayer('Optimal Player O', PlayOption.O, TIME_TO_WAIT_AFTER_PLAYING_MOVE_IN_SECONDS)

HUMAN_PLAYER_X = HumanPlayer('Human Player X', PlayOption.X)
HUMAN_PLAYER_O = HumanPlayer('Human Player O', PlayOption.O)

DISTRACTED_PLAYER_X = DistractedPlayer('Distracted Player X', PlayOption.X, ERROR_PROBABILITY_FOR_DISTRACTED_PLAYER, TIME_TO_WAIT_AFTER_PLAYING_MOVE_IN_SECONDS)
DISTRACTED_PLAYER_O = DistractedPlayer('Distracted Player O', PlayOption.O, ERROR_PROBABILITY_FOR_DISTRACTED_PLAYER, TIME_TO_WAIT_AFTER_PLAYING_MOVE_IN_SECONDS)
