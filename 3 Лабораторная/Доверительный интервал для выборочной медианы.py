import math


def calculate_median(arr: list):
    s_arr = sorted(arr)
    index = len(arr) // 2
    return (s_arr[index] + s_arr[index - 1]) / 2


def estimate_pdf(sample: list, x: float):
    # Гауссовское ядро
    def k(x):
        return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)

    def dk(x):
        return -x * k(x)

    def calculate_optimal_h(sample: list, eps=0.01):
        def iteration(prev_h: float):
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

        while abs(cur_h - prev_h) <= eps:
            cur_h, prev_h = iteration(prev_h) / len(sample), cur_h

        return cur_h

    h = calculate_optimal_h(sample)
    print(h)

    kernel_values = [k((x - y) / h) for y in sample]
    pdf_estimate = sum(kernel_values) / (h * len(sample))

    return pdf_estimate


def calculate_dispersion(sample: list, x: float):
    return 1 / (4 * estimate_pdf(sample, x) ** 2)


# Нормальное распределение
def quantile(p: float):
    return 4.91 * (p ** 0.14 - (1 - p) ** 0.14)


def confidence_interval(sample: list, betta: float):
    t_betta = quantile((1 + betta) / 2)
    sqrt_n = math.sqrt((len(sample)))
    median = calculate_median(sample)
    sqrt_dispersion = math.sqrt(calculate_dispersion(sample, median))
    return median - t_betta / sqrt_n * sqrt_dispersion, median + t_betta / sqrt_n * sqrt_dispersion


if __name__ == "__main__":
    path, betta = input().split()
    file = open(path, 'r')

    numbers = file.readlines()
    numbers = list(map(float, numbers))

    print(" ".join(f"{boundary:.5f}" for boundary in confidence_interval(numbers, float(betta))))

    file.close()
