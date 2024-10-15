from math import sqrt


def central_moment_ectimate(sample: list, k: int) -> float:
    n = len(sample)
    avg = sum(sample) / n

    moment_sum = 0
    for i in range(n):
        moment_sum += (sample[i] - avg) ** k

    central_moment = moment_sum / n

    return central_moment


def dispersion(sample: list) -> float:
    n = len(sample)
    avr = sum(sample) / n

    sum_diff = 0
    for i in range(n):
        sum_diff += (sample[i] - avr) ** 2

    sample_dispersion = sum_diff / (n - 1)

    return sample_dispersion


def coefficient_excess(sample: list) -> float:
    fourth_central_moment = central_moment_ectimate(sample, 4)
    standard_deviation = sqrt(dispersion(sample)) ** 4

    return fourth_central_moment / standard_deviation - 3


if __name__ == "__main__":
    file_path = input()

    with open(file_path, "r") as file:
        sample = file.readline().split()
        sample = list(map(float, sample))

    coef_excess = coefficient_excess(sample)

    print(f"{coef_excess:.5f}")
