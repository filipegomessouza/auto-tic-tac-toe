from typing import Optional, List
from src.enums.play_option import PlayOption
from src.exceptions.invalid_position_exception import InvalidPositionException
from src.exceptions.unavailable_position_exception import UnavailablePositionException
from src.enums.result import Result

class Board():
    BOARD_SIZE = 3

    def __init__(self):
        self.__board: List[List[Optional[PlayOption]]] = [
            [None] * self.BOARD_SIZE for _ in range(self.BOARD_SIZE)
        ]
        self.__filled_positions: int = 0

    def set(self, play_option: PlayOption, i: int, j: int) -> 'Board':
        if not self.__is_valid_position(i, j):
            raise InvalidPositionException('Position is out of bounds.')

        if not self.__is_available_position(i, j):
            raise UnavailablePositionException(f'Position ({i}, {j}) is not empty.')

        self.__board[i][j] = play_option
        self.__filled_positions += 1

        return self

    def __is_valid_position(self, i: int, j: int) -> bool:
        return 0 <= i < self.BOARD_SIZE and 0 <= j < self.BOARD_SIZE

    def __is_available_position(self, i: int, j: int) -> bool:
        return self.__board[i][j] is None

    def eval_result(self) -> Optional[Result]:
        if self.__filled_positions >= self.BOARD_SIZE ** 2:
            return Result.DRAW

        return self.__eval_result_in_lines() or self.__eval_result_in_columns() or self.__eval_result_in_diagonals()

    def __eval_result_in_lines(self) -> Optional[Result]:
        for line in self.__board:
            if line[0] is not None and line[0] == line[1] and line[1] == line[2]:
                return Result.PLAYER_O if line[0] == PlayOption.O else Result.PLAYER_X

        return None

    def __eval_result_in_columns(self) -> Optional[Result]:
        for j in range(self.BOARD_SIZE):
            if self.__board[0][j] is not None and self.__board[0][j] == self.__board[1][j] and self.__board[1][j] == self.__board[2][j]:
                return Result.PLAYER_O if self.__board[0][j] == PlayOption.O else Result.PLAYER_X

        return None

    def __eval_result_in_diagonals(self) -> Optional[Result]:
        if self.__board[0][0] is not None and self.__board[0][0] == self.__board[1][1] and self.__board[1][1] == self.__board[2][2]:
            return Result.PLAYER_O if self.__board[0][0] == PlayOption.O else Result.PLAYER_X

        if self.__board[0][2] is not None and self.__board[0][2] == self.__board[1][1] and self.__board[1][1] == self.__board[2][0]:
            return Result.PLAYER_O if self.__board[0][2] == PlayOption.O else Result.PLAYER_X

        return None

    def __str__(self):
        str_board = '┌───┬───┬───┐\n'

        for i, line in enumerate(self.__board):
            str_board += '│'
            for play_option in line:
                str_board += '   │' if play_option is None else f' {play_option.value} │'

            str_board += '\n├───┼───┼───┤\n' if i < 2 else '\n└───┴───┴───┘\n'

        return str_board
