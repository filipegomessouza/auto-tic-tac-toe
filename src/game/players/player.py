from typing import Tuple
from abc import ABC, abstractmethod
from src.enums.play_option import PlayOption
from src.game.board import Board

class Player(ABC):
    def __init__(self, name: str, play_option: PlayOption):
        self.__name = name
        self.__play_option = play_option

    @abstractmethod
    def play(self, board: Board) -> Tuple[int, int]:
        pass

    @property
    def name(self) -> str:
        return self.__name

    @property
    def play_option(self) -> PlayOption:
        return self.__play_option

    def set_play_option(self, play_option: PlayOption):
        self.__play_option = play_option
