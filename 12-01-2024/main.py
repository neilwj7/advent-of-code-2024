from solution import solution


def log(msg):
    print(msg)


if __name__ == "__main__":
    solution = solution("input.txt")
    result = solution.similarity()

    log(result)
