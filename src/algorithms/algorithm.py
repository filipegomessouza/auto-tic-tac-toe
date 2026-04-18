from abc import ABC, abstractmethod
from src.game.players.player import Player

class Algorithm(ABC):
    @abstractmethod
    def run(self) -> Player:
        pass
