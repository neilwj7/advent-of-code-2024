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
    
    
    def countValidReportsDamping(self):
        res = 0
        for report in self.reports:
            if self.validReportWithDamping(report):
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
    

    # assumes length of at least 3
    def validReportWithDamping(self, report):
        if abs(report[0] - report[1]) > 3:
            return self.validReport(report[1:]) or self.validReport(report[:1] + report[2:])

        # figure out direction
        direction = False
        if report[0] < report[1] and report[1] < report[2]:
            direction = True
        elif report[0] > report[1] and report[1] > report[2]:
            direction = False
        else:
            # already inconsistency in first three values: just try removing each of them individually and see if it works
            return self.validReport(report[1:]) + self.validReport(report[0:1] + report[2:]) + self.validReport(report[0:2] + report[3:])

        rmUsed = False
        skipFlag = False
        i = 1
        while True:
            if i == len(report) - 1 or (i == len(report) - 2 and skipFlag):
                break
            if skipFlag:
                skipFlag = False
                
                # next value is same as current: no change which is not allowed
                if report[i] == report[i + 2]:
                    return False
                
                
                # next value is decreasing but should be increasing
                if report[i] > report[i + 2] and direction:
                    return False

                # next value is increasing but should be decreasing
                if report[i] < report[i + 2] and not direction:
                    return False
                
                # next value is too large of a jump away
                if abs(report[i] - report[i + 2]) > 3:
                    return False
                
                i += 2
                continue

            # next value is same as current: no change which is not allowed
            if report[i] == report[i + 1]:
                if rmUsed:
                    return False
                rmUsed = True
                skipFlag = True
                if i == len(report) - 1:
                    return True
                continue
            
            
            # next value is decreasing but should be increasing
            if report[i] > report[i + 1] and direction:
                if rmUsed:
                    return False
                
                rmUsed = True
                skipFlag = True
                if i == len(report) - 2:
                    return True
                continue

            # next value is increasing but should be decreasing
            if report[i] < report[i + 1] and not direction:
                if rmUsed:
                    return False
                rmUsed = True
                skipFlag = True
                if i == len(report) - 2:
                    return True
                continue
            
            # next value is too large of a jump away
            if abs(report[i] - report[i + 1]) > 3:
                if rmUsed:
                    return False
                rmUsed = True
                skipFlag = True
                if i == len(report) - 2:
                    return True
                continue

            i += 1

        return True