import os
from typing import Optional
from src.game.board import Board
from src.game.players.player import Player
from src.exceptions.board_exception import BoardException
from src.exceptions.players_with_equal_play_option_exception import PlayersWithEqualPlayOptionException
from src.enums.result import Result

class TicTacToeGame:
    def __init__(self, should_render: bool = True) -> None:
        self.__should_render = should_render
        self.__board = Board()

    def run(self, player_one: Player, player_two: Player) -> Optional[Player]:
        self.__board.reset_board()
        self.__player_one = player_one
        self.__player_two = player_two
        self.__validate_players()
        self.__current_player = self.__player_one
        self.__result = None
        self.__render()

        while True:
            is_valid_play = self.__play()

            if not is_valid_play:
                continue

            self.__result = self.__board.eval_result()

            if self.__result is not None:
                break

            self.__current_player = self.__next_player()
            self.__render()

        self.__render()

        if self.__result == Result.DRAW:
            return None

        if self.__player_one.play_option.result() == self.__result:
            return self.__player_one

        return self.__player_two

    def __play(self) -> bool:
        is_valid_play = True

        try:
            self.__current_player.play(self.__board)
        except BoardException as e:
            is_valid_play = False
            print(e)

        return is_valid_play

    def __next_player(self) -> Player:
        return self.__player_two if self.__current_player is self.__player_one else self.__player_one

    def __render(self) -> None:
        if not self.__should_render:
            return

        self.__clear_console()
        print(self.__board)

        if self.__result is None:
            print(f"{self.__current_player.name}'s turn ({self.__current_player.play_option.value})")
        else:
            print('Game over! Result:', self.__result.value)

            if self.__result != Result.DRAW:
                winner = self.__player_one if self.__player_one.play_option.result() == self.__result else self.__player_two
                print('Winner:', winner.name)

    def __clear_console(self) -> None:
        os.system('clear' if os.name == 'posix' else 'cls')

    def __validate_players(self) -> None:
        if self.__player_one.play_option == self.__player_two.play_option:
            raise PlayersWithEqualPlayOptionException('Players cannot have the same play option.')

    def swap_players(self) -> None:
        self.__player_one, self.__player_two = self.__player_two, self.__player_one