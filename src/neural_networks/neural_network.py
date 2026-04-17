from abc import ABC, abstractmethod
from typing import List
import numpy as np

class NeuralNetwork(ABC):
    @abstractmethod
    def forward(self, input_layer: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def get_weights(self) -> np.ndarray:
        pass

    @abstractmethod
    def set_weights(self, weights: np.ndarray):
        pass
