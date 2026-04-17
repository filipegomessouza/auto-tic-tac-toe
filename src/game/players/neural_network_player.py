from typing import Optional, List, Tuple
from src.game.players.player import Player
from src.game.board import Board
from src.enums.play_option import PlayOption
from src.neural_networks.neural_network import NeuralNetwork
from src.enums.play_option import PlayOption
import numpy as np
import time

class NeuralNetworkPlayer(Player):
    def __init__(self, name: str, play_option: PlayOption, neural_network: NeuralNetwork, time_to_wait_after_playing_move_in_seconds: Optional[float] = None):
        super().__init__(name, play_option)
        self.__neural_network = neural_network
        self.__time_to_wait_after_playing_move_in_seconds = time_to_wait_after_playing_move_in_seconds

    def play(self, board: Board) -> None:
        input_layer = self.__get_input_layer(board)
        output_layer = self.__neural_network.forward(input_layer)

        print('INPUT LAYER:', input_layer)
        print('OUTPUT LAYER:', output_layer)
        print()

        i, j = self.__get_best_move(input_layer, output_layer, board)
        board.set(self.play_option, i, j)

        if self.__time_to_wait_after_playing_move_in_seconds is not None:
            time.sleep(self.__time_to_wait_after_playing_move_in_seconds)

    def __get_input_layer(self, board: Board) -> np.ndarray:
        arr_board = board.get_arr_board()
        input_layer: List[int] = []

        for line in arr_board:
            for cell in line:
                input_layer.append(self.__node_value(cell))

        return np.array(input_layer)

    def __get_best_move(self, input_layer: np.ndarray, output_layer: np.ndarray, board: Board) -> Tuple[int, int]:
        max_value = float('-inf')
        best_index = -1

        for i in range(len(output_layer)):
            if input_layer[i] == 0 and output_layer[i] > max_value:
                max_value = output_layer[i]
                best_index = i

        i = best_index // board.BOARD_SIZE
        j = best_index % board.BOARD_SIZE

        return i, j

    def __node_value(self, play_option: Optional[PlayOption]) -> int:
        if play_option is None:
            return 0

        if self.play_option == play_option:
            return 1

        return -1

