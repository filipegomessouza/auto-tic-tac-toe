from typing import Optional, List, Tuple
from src.enums.play_option import PlayOption
from src.exceptions.invalid_position_exception import InvalidPositionException
from src.exceptions.unavailable_position_exception import UnavailablePositionException
from src.enums.result import Result
import copy

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

        return self.force_set(play_option, i, j)

    def force_set(self, play_option: Optional[PlayOption], i: int, j: int) -> 'Board':
        old_play_option = self.__board[i][j]
        self.__board[i][j] = play_option

        if old_play_option is None and play_option is not None:
            self.__filled_positions += 1
        elif old_play_option is not None and play_option is None:
            self.__filled_positions -= 1

        return self
    def __is_valid_position(self, i: int, j: int) -> bool:
        return 0 <= i < self.BOARD_SIZE and 0 <= j < self.BOARD_SIZE

    def __is_available_position(self, i: int, j: int) -> bool:
        return self.__board[i][j] is None

    def eval_result(self) -> Optional[Result]:
        result = self.__eval_result_in_lines() or self.__eval_result_in_columns() or self.__eval_result_in_diagonals()

        if result is not None:
            return result

        if self.__filled_positions >= self.BOARD_SIZE ** 2:
            return Result.DRAW

        return None

    def __eval_result_in_lines(self) -> Optional[Result]:
        for line in self.__board:
            if line[0] is not None and all(cell == line[0] for cell in line):
                return Result.PLAYER_O if line[0] == PlayOption.O else Result.PLAYER_X

        return None

    def __eval_result_in_columns(self) -> Optional[Result]:
        for j in range(self.BOARD_SIZE):
            if self.__board[0][j] is not None and all(self.__board[i][j] == self.__board[0][j] for i in range(self.BOARD_SIZE)):
                return Result.PLAYER_O if self.__board[0][j] == PlayOption.O else Result.PLAYER_X

        return None

    def __eval_result_in_diagonals(self) -> Optional[Result]:
        if self.__board[0][0] is not None and all(self.__board[i][i] == self.__board[0][0] for i in range(self.BOARD_SIZE)):
            return Result.PLAYER_O if self.__board[0][0] == PlayOption.O else Result.PLAYER_X

        if self.__board[0][self.BOARD_SIZE - 1] is not None and all(self.__board[i][self.BOARD_SIZE - 1 - i] == self.__board[0][self.BOARD_SIZE - 1] for i in range(self.BOARD_SIZE)):
            return Result.PLAYER_O if self.__board[0][self.BOARD_SIZE - 1] == PlayOption.O else Result.PLAYER_X

        return None

    def available_positions(self) -> List[Tuple[int, int]]:
        return [(i, j) for i in range(self.BOARD_SIZE) for j in range(self.BOARD_SIZE) if self.__board[i][j] is None]

    def __str__(self):
        str_board = '    '

        for j in range(self.BOARD_SIZE):
            str_board += f'{j}   '

        str_board += '\n  ┌' + '───┬' * (self.BOARD_SIZE - 1) + '───┐\n'

        for i, line in enumerate(self.__board):
            str_board += f'{i} │'
            for play_option in line:
                str_board += '   │' if play_option is None else f' {play_option.value} │'

            if i < self.BOARD_SIZE - 1:
                str_board += '\n  ├' + '───┼' * (self.BOARD_SIZE - 1) + '───┤\n'
            else:
                str_board += '\n  └' + '───┴' * (self.BOARD_SIZE - 1) + '───┘\n'

        return str_board

    def get_arr_board(self) -> List[List[Optional[PlayOption]]]:
        return copy.deepcopy(self.__board)