from solution import solution


def log(msg):
    print(msg)


if __name__ == "__main__":
    solution = solution("input.txt")
    result1 = solution.countValidReports()
    log(result1)

    result2 = solution.countValidReportsDamping()
    log(result2)

