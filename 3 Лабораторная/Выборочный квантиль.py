def selective_quantile(numbers: list, a: float) -> float:
    n = len(numbers)
    k = int(a * n) + 1

    if k == 0:
        return numbers[0]
    elif k >= n:
        return numbers[-1]
    else:
        return numbers[k - 1] + (n * a - k + 1) * (numbers[k] - numbers[k - 1])


if __name__ == "__main__":
    input_data = input()
    file_path, a = input_data.split()
    a = float(a)

    with open(file_path, "r") as file:
        numbers = file.readline().split()
        numbers = list(map(float, numbers))

    numbers.sort()

    quantile = selective_quantile(numbers, a)

    print(f"{quantile:.5f}")
