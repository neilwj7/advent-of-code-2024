from solution import solution


def log(msg):
    print(msg)


if __name__ == "__main__":
    solution = solution('input.txt')
    result1 = solution.solve(0)
    log(result1)
    result2 = solution.solve(10000000000000)
    log(result2)
