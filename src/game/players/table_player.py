from typing import Dict, List, Optional, Tuple
from src.game.players.player import Player
from src.game.board import Board
from src.enums.play_option import PlayOption
from src.enums.result import Result
import time
import random

_BOARD_SIZE = 3
_NUM_CELLS = _BOARD_SIZE * _BOARD_SIZE
_LINES = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

BoardKey = Tuple[Optional[PlayOption], ...]
StateKey = Tuple[BoardKey, PlayOption]
PolicyEntry = Tuple[Tuple[int, int], int]


class TablePlayer(Player):
    def __init__(self, name: str, play_option: PlayOption, time_to_wait_after_playing_move_in_seconds: Optional[float] = None) -> None:
        super().__init__(name, play_option)
        self.__time_to_wait_after_playing_move_in_seconds = time_to_wait_after_playing_move_in_seconds
        self.__table: Dict[StateKey, PolicyEntry] = {}
        self.__build_table()

    def play(self, board: Board) -> None:
        positions = board.available_positions()

        if len(positions) == board.BOARD_SIZE ** 2:
            i, j = random.choice(positions)
        else:
            board_key: BoardKey = tuple(cell for row in board.get_arr_board() for cell in row)
            (i, j), _ = self.__table[(board_key, self.play_option)]

        board.set(self.play_option, i, j)

        if self.__time_to_wait_after_playing_move_in_seconds is not None:
            time.sleep(self.__time_to_wait_after_playing_move_in_seconds)

    def __build_table(self) -> None:
        board: List[Optional[PlayOption]] = [None] * _NUM_CELLS

        for play_option in (PlayOption.X, PlayOption.O):
            self.__solve(board, play_option)

    def __solve(self, board: List[Optional[PlayOption]], play_option: PlayOption) -> int:
        key: StateKey = (tuple(board), play_option)

        if key in self.__table:
            _, cached_score = self.__table[key]
            return cached_score

        result = self.__terminal(board)

        if result is not None:
            score = self.__score_result(result, play_option)
            self.__table[key] = ((-1, -1), score)
            return score

        best_score = float('-inf')
        best_move: Tuple[int, int] = (-1, -1)
        opponent = play_option.opposite()

        for idx in range(_NUM_CELLS):
            if board[idx] is not None:
                continue

            board[idx] = play_option
            opponent_score = self.__solve(board, opponent)
            score = -opponent_score
            board[idx] = None

            if score > best_score:
                best_score = score
                best_move = (idx // _BOARD_SIZE, idx % _BOARD_SIZE)

        final_score = int(best_score)
        self.__table[key] = (best_move, final_score)

        return final_score

    def __terminal(self, board: List[Optional[PlayOption]]) -> Optional[Result]:
        for a, b, c in _LINES:
            if board[a] is not None and board[a] == board[b] == board[c]:
                return Result.PLAYER_O if board[a] == PlayOption.O else Result.PLAYER_X

        if all(cell is not None for cell in board):
            return Result.DRAW

        return None

    def __score_result(self, result: Result, play_option: PlayOption) -> int:
        if result == Result.DRAW:
            return 0

        return 1 if result == play_option.result() else -1
