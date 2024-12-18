from solution import solution


def log(msg):
    print(msg)


if __name__ == "__main__":
    solution = solution('input.txt')
    result1 = solution.countTotalCalibration()
    log(result1)
    result2 = solution.countTotalCalibrationWithConcat()
    log(result2)
