from enum import Enum

from src.enums.result import Result

class PlayOption(Enum):
    O = 'O'
    X = 'X'

    def opposite(self) -> 'PlayOption':
        return PlayOption.O if self == PlayOption.X else PlayOption.X

    def result(self) -> 'Result':
        return Result.PLAYER_O if self == PlayOption.O else Result.PLAYER_X
