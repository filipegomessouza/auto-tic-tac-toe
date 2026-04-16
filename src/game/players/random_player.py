from typing import Optional
from src.game.players.player import Player
from src.game.board import Board
from src.enums.play_option import PlayOption
import random
import time

class RandomPlayer(Player):
    def __init__(self, name: str, play_option: PlayOption, time_to_wait_after_playing_move_in_seconds: Optional[float] = None):
        super().__init__(name, play_option)
        self.__time_to_wait_after_playing_move_in_seconds = time_to_wait_after_playing_move_in_seconds

    def play(self, board: Board) -> None:
        i, j = random.choice(board.available_positions())
        board.set(self.play_option, i, j)

        if self.__time_to_wait_after_playing_move_in_seconds is not None:
            time.sleep(self.__time_to_wait_after_playing_move_in_seconds)
