from typing import Tuple
from src.game.players.player import Player
from src.game.board import Board
from src.enums.play_option import PlayOption

class HumanPlayer(Player):
    def __init__(self, name: str, play_option: PlayOption):
        super().__init__(name, play_option)

    def play(self, board: Board) -> Tuple[int, int]:
        i, j = self.__get_cli_input()
        board.set(self.play_option, i, j)

        return i, j

    def __get_cli_input(self) -> Tuple[int, int]:
        while True:
            cli_input_arguments = input('Enter position (row col): ').split()

            if len(cli_input_arguments) != 2:
                print('Invalid input: expected 2 arguments (row col).')
                continue

            i, j = cli_input_arguments

            if not i.isdigit() or not j.isdigit():
                print('Invalid input: coordinates must be positive integers.')
                continue

            return int(i), int(j)
