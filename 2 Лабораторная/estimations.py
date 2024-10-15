from abc import ABC
from typing import Optional

import numpy as np


class Estimation(ABC):
    def __init__(self, sample: np.ndarray) -> None:
        self.sample = sample


class EDF(Estimation):
    def heaviside_function(x: float) -> int:
        return 1 if x > 0 else 0

    def value(self, x: np.ndarray) -> np.ndarray:
        return np.mean(np.vectorize(EDF.heaviside_function)(x - self.sample))


class Histogram(Estimation):
    class Interval:
        def __init__(self, a: float, b: float) -> None:
            self.a = a
            self.b = b

        def is_in(self, x: float) -> bool:
            return self.a <= x < self.b

        def __repr__(self) -> str:
            return f'({self.a}, {self.b})'

    def __init__(self, sample: np.ndarray, m: int) -> None:
        super().__init__(sample)
        self.m = m
        self.init_intervals()

    def init_intervals(self) -> None:
        left_boundary_of_intervals = np.linspace(np.min(self.sample), np.max(self.sample), self.m + 1)[:-1]
        right_boundary_of_intervals = np.concatenate((left_boundary_of_intervals[1:], [np.max(self.sample)]))

        self.intervals = [Histogram.Interval(a, b) for a, b in
                          zip(left_boundary_of_intervals, right_boundary_of_intervals)]

        self.sub_interval_width = right_boundary_of_intervals[0] - left_boundary_of_intervals[0]

    def get_interval(self, x: float) -> Optional[Interval]:
        for i in self.intervals:
            if i.is_in(x):
                return i
        return None

    def get_sample_by_interval(self, interval: Interval) -> np.ndarray:
        return np.array(list(filter(lambda x: interval.is_in(x), self.sample)))

    def value(self, x: float) -> float:
        interval = self.get_interval(x)
        if interval is not None:
            sample_by_interval = self.get_sample_by_interval(interval)
            return len(sample_by_interval) / (self.sub_interval_width * len(self.sample))
        return 0.0
