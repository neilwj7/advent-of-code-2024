class solution:
    def __init__(self, inputFile):
        self.reports = self.getInput(inputFile)
    
    def getInput(self, fileName):
        res = []
        with open(fileName, 'r') as file:
            for line in file:
                res.append([int(x) for x in line.strip().split()])
        return res
    
    def solveP1(self):
        res = 0
        for report in self.reports:
            if self.validReport(report): res += 1
        return res
    
    def solveP2(self):
        res = 0
        for report in self.reports:
            for i in range(len(report)):
                if self.validReport(report[0:i] + report[i + 1:]):
                    res += 1
                    break
        return res
    
    def validReport(self, report):
        increasing = report[0] < report[1]
        for i in range(1, len(report)):
            diff = report[i] - report[i - 1]
            if (abs(diff) > 3 or diff == 0) or (diff > 0 and not increasing) or (diff < 0 and increasing): return False
        return True