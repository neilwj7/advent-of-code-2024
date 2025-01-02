from solution import solution


def log(msg):
    print(msg)


if __name__ == "__main__":
    solution = solution('input.txt')
    result1 = solution.solveP1()
    log(result1)
    result2 = solution.solveP2()
    for wire in result2: print(wire, end=',')
    print()