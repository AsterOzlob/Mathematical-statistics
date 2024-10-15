def central_moment_ectimate(numbers: list, k: int):
    n = len(numbers)
    avg = sum(numbers) / n

    moment_sum = 0
    for i in range(n):
        moment_sum += (numbers[i] - avg) ** k

    central_moment = moment_sum / n

    return central_moment


if __name__ == "__main__":
    input_data = input()
    file_path, k = input_data.split()
    k = int(k)

    with open(file_path, 'r') as file:
        numbers = file.readline().split()
        numbers = list(map(float, numbers))

    central_moment = central_moment_ectimate(numbers, k)

    print(round(central_moment, 5))
