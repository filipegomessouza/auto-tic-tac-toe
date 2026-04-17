from src.neural_networks.neural_network import NeuralNetwork
import numpy as np

class OneHiddenLayerNeuralNetwork(NeuralNetwork):
    def __init__(self, input_size, hidden_size, output_size):
        self.__input_size  = input_size
        self.__hidden_size = hidden_size
        self.__output_size = output_size

        self.W1 = np.random.randn(input_size, hidden_size) * 0.5
        self.b1 = np.zeros(hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size) * 0.5
        self.b2 = np.zeros(output_size)

    def forward(self, x):
        z1 = x @ self.W1 + self.b1
        h  = self.__relu(z1)
        z2 = h @ self.W2 + self.b2

        return z2

    def get_weights(self) -> np.ndarray:
        return np.concatenate([
            self.W1.flatten(),
            self.b1,
            self.W2.flatten(),
            self.b2
        ])

    def set_weights(self, vetor: np.ndarray):
        i0 = 0
        i1 = self.__input_size * self.__hidden_size
        i2 = i1 + self.__hidden_size
        i3 = i2 + self.__hidden_size * self.__output_size
        i4 = i3 + self.__output_size

        self.W1 = vetor[i0:i1].reshape(self.__input_size, self.__hidden_size)
        self.b1 = vetor[i1:i2]
        self.W2 = vetor[i2:i3].reshape(self.__hidden_size, self.__output_size)
        self.b2 = vetor[i3:i4]

    def __relu(value: np.ndarray) -> np.ndarray:
        return np.maximum(0, value)