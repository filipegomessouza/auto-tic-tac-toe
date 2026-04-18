from typing import Tuple, Optional
from src.game.players.player import Player
from src.game.board import Board
from src.enums.play_option import PlayOption
from src.enums.result import Result
import time
import random

class MiniMaxPlayer(Player):
    def __init__(self, name: str, play_option: PlayOption, time_to_wait_after_playing_move_in_seconds: Optional[float] = None) -> None:
        super().__init__(name, play_option)
        self.__time_to_wait_after_playing_move_in_seconds = time_to_wait_after_playing_move_in_seconds

    def play(self, board: Board) -> None:
        positions = board.available_positions()
        i, j = random.choice(positions) if len(positions) == board.BOARD_SIZE ** 2 else self.__minimax(board)

        board.set(self.play_option, i, j)

        if self.__time_to_wait_after_playing_move_in_seconds is not None:
            time.sleep(self.__time_to_wait_after_playing_move_in_seconds)

    def __minimax(self, board: Board) -> Tuple[int, int]:
        best_value = float('-inf')
        best_move = (-1, -1)

        for i, j in board.available_positions():
            board.force_set(self.play_option, i, j)

            value = self.__minimize(board)

            if value > best_value or value == best_value and random.choice([True, False]):
                best_value = value
                best_move = (i, j)

            board.force_set(None, i, j)

        return best_move

    def __maximize(self, board: Board) -> int:
        score = self.__score(board)

        if score is not None:
            return score

        best_value = float('-inf')

        for i, j in board.available_positions():
            board.force_set(self.play_option, i, j)

            value = self.__minimize(board)
            best_value = max(best_value, value)
            board.force_set(None, i, j)

        return best_value

    def __minimize(self, board: Board) -> int:
        score = self.__score(board)

        if score is not None:
            return score

        worst_value = float('inf')

        for i, j in board.available_positions():
            board.force_set(self.play_option.opposite(), i, j)

            value = self.__maximize(board)
            worst_value = min(worst_value, value)
            board.force_set(None, i, j)

        return worst_value

    def __score(self, board: Board) -> Optional[int]:
        result = board.eval_result()

        if result is None:
            return None

        if result == Result.DRAW:
            return 0

        if result == self.play_option.result():
            return 1

        return -1
