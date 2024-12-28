from solution import solution


def log(msg):
    print(msg)


if __name__ == "__main__":
    solution = solution(71, 'input.txt')
    result1 = solution.solveP1(1024)
    log(result1)
    result2 = solution.solveP2()
    log(result2)