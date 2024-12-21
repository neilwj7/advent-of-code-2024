from solution import solution


def log(msg):
    print(msg)


if __name__ == "__main__":
    solution = solution('input.txt', 101, 103)
    result1 = solution.solveP1()
    log(result1)
    result2 = solution.solveP2()
    log(result2)
