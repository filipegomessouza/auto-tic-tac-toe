from typing import Tuple
from src.game.players.player import Player
from src.game.board import Board
from src.exceptions.invalid_cli_input import InvalidCliInputException
from src.enums.play_option import PlayOption

class HumanPlayer(Player):
    def __init__(self, name: str, play_option: PlayOption):
        super().__init__(name, play_option)

    def play(self, board: Board) -> None:
        i, j = self.__get_cli_input()

        board.set(self.play_option, i, j)

    def __get_cli_input(self) -> Tuple[int, int]:
        cli_input_arguments = input().split(' ')

        if len(cli_input_arguments) != 2:
            raise InvalidCliInputException('Invalid input: expected 2 arguments.')

        i, j = cli_input_arguments

        if not i.isdigit() or not j.isdigit():
            raise InvalidCliInputException('Invalid input: coordinates must be positive integers.')

        return int(i), int(j)