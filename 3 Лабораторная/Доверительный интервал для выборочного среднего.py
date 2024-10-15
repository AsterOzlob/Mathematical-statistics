 import math


def calculate_mean(sample: list) -> float:
    return sum(sample) / len(sample)


def calculate_dispersion(sample: list, mean: float) -> float:
    return sum(map(lambda x: (x - mean) ** 2, sample)) / (len(sample) - 1)


def confidence_interval(sample: list, betta: float, mean: float):
    quantiles = {0.9: 1.6602, 0.95: 1.984, 0.99: 2.6259}
    t_betta = quantiles[betta]
    sqrt_n = math.sqrt((len(sample)))
    sqrt_dispersion = math.sqrt(calculate_dispersion(sample, mean))
    return (mean - t_betta / sqrt_n * sqrt_dispersion,
            mean + t_betta / sqrt_n * sqrt_dispersion)


if __name__ == "__main__":
    path, betta = input().split()
    file = open(path, 'r')

    numbers = file.readline().split()
    numbers = list(map(float, numbers))

    mean = calculate_mean(numbers)

    print(" ".join(f"{boundary:.5f}" for boundary in confidence_interval(numbers, float(betta), mean)))

    file.close()
