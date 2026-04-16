from src.game.players.player import Player
from src.game.board import Board
from src.enums.play_option import PlayOption
import random
import time

class RandomPlayer(Player):
    def __init__(self, name: str, play_option: PlayOption):
        super().__init__(name, play_option)

    def play(self, board: Board) -> None:
        i, j = random.choice(board.available_positions())
        board.set(self.play_option, i, j)

        time.sleep(0.4)
