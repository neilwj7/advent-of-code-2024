class solution:
    def __init__(self, inputFile):
        self.reports = self.getReports(inputFile)
    

    def getReports(self, inputFile):
        res = []
        with open(inputFile, 'r') as file:
            for line in file:
                report = []
                reportS = line.split()
                for s in reportS:
                    report.append(int(s))
                res.append(report)
        return res
    

    def countValidReports(self):
        res = 0
        for report in self.reports:
            if self.validReport(report):
                res += 1
        return res
    

    def validReport(self, report):
        if len(report) <= 1:
            return True
        
        if report[0] == report[1]:
            return False
        
        if abs(report[0] - report[1]) > 3:
            return False

        direction = report[0] < report[1]

        for i in range(1, len(report) - 1):
            # next value is same as current: no change which is not allowed
            if report[i] == report[i + 1]:
                return False
            
            # next value is decreasing but should be increasing
            if report[i] > report[i + 1] and direction:
                return False

            # next value is increasing but should be decreasing
            if report[i] < report[i + 1] and not direction:
                return False
            
            # next value is too large of a jump away
            if abs(report[i] - report[i + 1]) > 3:
                return False
        
        return True