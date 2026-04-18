from typing import Optional
from src.game.players.player import Player
from src.game.board import Board
from src.enums.play_option import PlayOption
from src.game.players.table_player import TablePlayer
from src.game.players.random_player import RandomPlayer
import random

class DistractedPlayer(Player):
    def __init__(self, name: str, play_option: PlayOption, error_probability: float, time_to_wait_after_playing_move_in_seconds: Optional[float] = None):
        super().__init__(name, play_option)
        self.__error_probability = error_probability
        self.__validate_error_probability()

        self.__optimal_player = TablePlayer(name, play_option, time_to_wait_after_playing_move_in_seconds)
        self.__random_player = RandomPlayer(name, play_option, time_to_wait_after_playing_move_in_seconds)

    def play(self, board: Board) -> None:
        player = self.__random_player if random.random() <= self.__error_probability else self.__optimal_player
        player.play(board)

    def set_error_probability(self, error_probability: float) -> None:
        self.__error_probability = error_probability
        self.__validate_error_probability()

    def __validate_error_probability(self) -> None:
        if self.__error_probability < 0 or self.__error_probability > 1:
            raise ValueError('Error probability must be between 0 and 1.')

    @property
    def error_probability(self) -> float:
        return self.__error_probability
