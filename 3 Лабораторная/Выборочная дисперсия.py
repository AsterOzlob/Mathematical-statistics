def dispersion(sample: list) -> float:
    n = len(sample)
    avr = sum(sample) / n

    sum_diff = 0
    for i in range(n):
        sum_diff += (sample[i] - avr) ** 2

    sample_dispersion = sum_diff / (n - 1)

    return sample_dispersion


if __name__ == "__main__":
    file_path = input()

    with open(file_path, "r") as file:
        sample = file.readline().split()
        sample = list(map(float, sample))

    sample_dispersion = dispersion(sample)

    print(round(sample_dispersion, 5))
