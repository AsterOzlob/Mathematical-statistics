from abc import ABC, abstractmethod
from random_variables import RandomVariable

import numpy as np


class RandomNumberGenerator(ABC):
    """
    @brief Abstract base class for random number generators.

    This class defines the interface for random number generators.
    Subclasses must implement the get() method.
    """

    def __init__(self, random_variable: RandomVariable) -> None:
        """
        @brief Initializes a new instance of the RandomNumberGenerator class.
        @param random_variable: The random variable used for generating numbers.
        """
        self.random_variable = random_variable

    @abstractmethod
    def get(self, N: int) -> np.ndarray:
        """
        @brief Generates random numbers.
        @param N: The number of random numbers to generate.
        @return: An array of random numbers.
        """
        pass


class SimpleRandomNumberGenerator(RandomNumberGenerator):
    """
    @brief Simple random number generator that uses quantile transformation.
    """

    def __init__(self, random_variable: RandomVariable) -> None:
        """
        @brief Initializes a new instance of the SimpleRandomNumberGenerator class.
        @param random_variable: The random variable used for generating numbers.
        """
        super().__init__(random_variable)

    def get(self, N: int) -> np.ndarray:
        """
        @brief Generates random numbers using the specified random variable.
        @param N: The number of random numbers to generate.
        @return: An array of random numbers.
        """
        us = np.random.uniform(0, 1, N)
        return np.vectorize(self.random_variable.quantile)(us)
