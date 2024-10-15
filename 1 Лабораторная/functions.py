import numpy as np
from numpy.random import randint


# Моделированние эксперимента
def flip_coin() -> int:
    return randint(0, 2)


# Моделирование N экспериментов
def experiment(n: int) -> np.array:
    result = np.zeros(n)
    counter = 0  # Частота выпадения
    for i in range(n):
        fc = flip_coin()
        if fc == 1:
            counter += 1
        result[i] = counter / (i + 1)
    return result


# Моделирование серий M по N экспериментов
def exp_serial(m: int, n: int) -> np.array:
    result = np.zeros((m, n))
    for i in range(m):
        result[i, :] = experiment(n)
    return result


# Функция вычисления средней частоты по столбцам
def mean(vs: np.array) -> np.array:
    return np.mean(vs, axis=0)


# Функция вычисления доверительного интервала
def conf_interval(vs: np.array, alpha: float) -> np.array:
    m = vs.shape[0]
    a = (1 - alpha) / 2
    m_down = int(m * a)
    m_up = m - m_down - 1

    sorted_vs = np.sort(vs, axis=0)

    return np.apply_along_axis(lambda x: np.array([x[m_down], x[m_up]]), 0, sorted_vs)


# Функция приближенного вычисления квантиля
# стандартного нормального распределения
def normal_quantile(p: float) -> float:
    return 4.91 * (p ** 0.14 - (1 - p) ** 0.14)
