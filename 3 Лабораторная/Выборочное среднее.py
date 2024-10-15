if __name__ == "__main__":
    file_path = input()

    file = open(file_path, "r")

    numbers = file.readline().split()
    numbers = list(map(float, numbers))

    print(round(1 / len(numbers) * sum(numbers), 5))

    file.close()
