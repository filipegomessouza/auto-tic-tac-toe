from abc import ABC, abstractmethod
from typing import List
import numpy as np

class NeuralNetwork(ABC):
    @abstractmethod
    def forward(self, input_layer: List[float]) -> List[float]:
        pass

    def get_weights(self) -> np.ndarray:
        pass
