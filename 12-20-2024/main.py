from solution import solution


def log(msg):
    print(msg)


if __name__ == "__main__":
    solution = solution('input.txt')
    result1 = solution.solve(100, 2)
    log(result1)
    result2 = solution.solve(100, 20)
    log(result2)
