def median(arr: list) -> float:
    return (arr[(len(arr) - 1) // 2] + arr[len(arr) // 2]) / 2


def hodges_lehmann_estimator(arr: list) -> float:
    walsh_average = [(arr[i] + arr[j]) / 2
                     for i in range(len(arr))
                     for j in range(i + 1, len(arr))]
    walsh_average.sort()
    return median(walsh_average)


if __name__ == '__main__':
    path = input()

    file = open(path, 'r')

    numbers = file.readline().split()
    numbers = list(map(float, numbers))

    print('{:.5f}'.format(hodges_lehmann_estimator(numbers)))

    file.close()
