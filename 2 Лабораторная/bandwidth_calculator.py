import math
import numpy as np


def calculate_bandwidth(sample: np.ndarray, eps: float = 0.01) -> float:
    def k(x: float) -> float:
        return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)

    def dk(x: float) -> float:
        return -x * k(x)

    def iteration(prev_h) -> float:
        result = 0

        for i in range(len(sample)):
            numerator = 0
            denominator = 0

            for j in range(len(sample)):
                if i != j:
                    diff = sample[i] - sample[j]
                    u = diff / prev_h
                    numerator += dk(u) * diff
                    denominator += k(u)

            # Проверка, чтобы избежать деления на ноль
            if denominator != 0:
                result += numerator / denominator

        return -result

    prev_h = 0.1
    cur_h = iteration(prev_h) / len(sample)

    while abs(cur_h - prev_h) > eps:
        prev_h, cur_h = cur_h, iteration(cur_h) / len(sample)

    return cur_h
