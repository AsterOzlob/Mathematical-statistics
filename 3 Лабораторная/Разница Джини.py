def gini(numbers: list) -> float:
    n = len(numbers)

    sum_diff = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum_diff += abs(numbers[i] - numbers[j])

    return (2 * sum_diff) / (n * (n - 1))


if __name__ == "__main__":
    file_path = input()

    with open(file_path, "r") as file:
        numbers = file.readline().split()
        numbers = list(map(float, numbers))

    gini_value = gini(numbers)

    print(round(gini_value, 5))
