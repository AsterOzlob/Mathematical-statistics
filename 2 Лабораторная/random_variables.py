from abc import ABC, abstractmethod
from estimations import Estimation

import math
import numpy as np


class RandomVariable(ABC):
    """
    @brief Abstract base class for random variables.

    This class provides the interface for random variables, which includes
    methods for calculating the probability density function (pdf), the
    cumulative distribution function (cdf), and the quantile function.
    """

    @abstractmethod
    def pdf(self, x: float) -> float:
        """
        @brief Computes the probability density function at a given point.

        @param x The point at which the pdf is evaluated.
        @return The probability density value at x.
        """
        pass

    @abstractmethod
    def cdf(self, x: float) -> float:
        """
        @brief Computes the cumulative distribution function at a given point.

        @param x The point at which the cdf is evaluated.
        @return The cumulative distribution value at x.
        """
        pass

    @abstractmethod
    def quantile(self, alpha: float) -> float:
        pass


class SmoothedRandomVariable(RandomVariable, Estimation):
    def __init__(self, sample: np.ndarray, h: float) -> None:
        super().__init__(sample)
        self.h = h

    def pdf(self, x: float) -> float:
        return np.mean([SmoothedRandomVariable.k((x - y) / self.h) for y in self.sample]) / self.h

    def cdf(self, x: float) -> float:
        return np.mean([SmoothedRandomVariable.K((x - y) / self.h) for y in self.sample])

    def quantile(self, alpha: float) -> None:
        raise NotImplementedError

    @staticmethod
    def K(x: float) -> float:
        if x >= 0:
            return 1 - 0.852 * math.exp(-((x + 1.5774) / 2.0637) ** 2.34)
        else:
            return 1 - (1 - 0.852 * math.exp(-((-x + 1.5774) / 2.0637) ** 2.34))

    @staticmethod
    def k(x: float) -> float: #
        return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)


class NormalRandomVariable(RandomVariable):
    def __init__(self, location: float = 0, scale: float = 1) -> None:
        super().__init__()
        self.location = location
        self.scale = scale

    def pdf(self, x: float) -> float:
        z = (x - self.location) / self.scale
        return math.exp(-0.5 * z * z) / (math.sqrt(2 * math.pi) * self.scale)

    def cdf(self, x: float) -> float:
        z = (x - self.location) / self.scale;
        if z <= 0:
            return 0.852 * math.exp(-math.pow((-z + 1.5774) / 2.0637, 2.34))
        return 1 - 0.852 * math.exp(-math.pow((z + 1.5774) / 2.0637, 2.34))

    def quantile(self, alpha: float) -> float:
        return self.location + 4.91 * self.scale * (math.pow(alpha, 0.14) - math.pow(1 - alpha, 0.14))


class UniformRandomVariable(RandomVariable):
    def __init__(self, a: float = 0, b: float = 1) -> None:
        super().__init__()
        self.a = a
        self.b = b

    def pdf(self, x: float) -> float:
        return 1.0 / (self.b - self.a) if self.a <= x <= self.b else 0

    def cdf(self, x: float) -> float:
        if x < self.a:
            return 0
        elif x > self.b:
            return 1
        else:
            return (x - self.a) / (self.b - self.a)

    def quantile(self, alpha: float) -> float:
        return self.a + alpha * (self.b - self.a)


class ExponentialRandomVariable(RandomVariable):
    def __init__(self, rate: float) -> None:
        if rate <= 0:
            raise ValueError("Rate must be positive")
        self.rate = rate

    def pdf(self, x: float) -> float:
        if x < 0:
            return 0
        return self.rate * math.exp(-self.rate * x)

    def cdf(self, x: float) -> float:
        if x < 0:
            return 0
        return 1 - math.exp(-self.rate * x)

    def quantile(self, alpha: float) -> float:
        if not 0 < alpha < 1:
            raise ValueError("Alpha must be between 0 and 1")
        return -math.log(1 - alpha) / self.rate


class LaplaceRandomVariable(RandomVariable):
    def __init__(self, location: float = 0, scale: float = 1) -> None:
        super().__init__()
        self.location = location
        self.scale = scale

    def pdf(self, x: float) -> float:
        return 0.5 * math.exp(-abs(x - self.location) / self.scale) / self.scale

    def cdf(self, x: float) -> float:
        if x < self.location:
            return 0.5 * math.exp((x - self.location) / self.scale)
        else:
            return 1 - 0.5 * math.exp(-(x - self.location) / self.scale)

    def quantile(self, alpha: float) -> float:
        if alpha < 0.5:
            return self.location + self.scale * math.log(2 * alpha)
        return self.location - self.scale * math.log(2 * (1 - alpha))


class CauchyRandomVariable(RandomVariable):
    def __init__(self, location: float = 0, scale: float = 1) -> None:
        self.location = location
        self.scale = scale

    def pdf(self, x: float) -> float:
        return 1 / (math.pi * self.scale * (1 + ((x - self.location) / self.scale) ** 2))

    def cdf(self, x: float) -> float:
        return 0.5 + math.atan((x - self.location) / self.scale) / math.pi

    def quantile(self, alpha: float) -> float:
        if not 0 < alpha < 1:
            raise ValueError("Alpha must be between 0 and 1")
        return self.location + self.scale * math.tan(math.pi * (alpha - 0.5))
