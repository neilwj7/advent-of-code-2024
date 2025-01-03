from copy import deepcopy
class solution:
    def __init__(self, inputFile):
        self.inputS = self.readInput(inputFile)
        self.filePositions, self.blankPositions = self.getLocations()
        self.workingS = self.createWorkingStr()

    def readInput(self, fileName):
        res = ""
        with open(fileName, 'r') as file:
            for line in file:
                res = line.strip()
        return res 

    def getLocations(self):
        fFlag = True
        i = 0
        curr = 0
        filePositions = [[0, 0] for i in range((len(self.inputS) // 2) + 1)]
        blankPositions = [[0, 0] for i in range(len(self.inputS) // 2)]
        for c in self.inputS:
            a = int(c)
            if fFlag:
                filePositions[i // 2] = [curr, curr + a - 1]
            else:
                blankPositions[i // 2] = [curr, curr + a - 1]
            i += 1
            curr = curr + a
            fFlag = not fFlag
        return filePositions, blankPositions

    def createWorkingStr(self):
        s = self.filePositions[0][1] + 1
        for i in range(len(self.blankPositions)):
            s += self.filePositions[i + 1][1] - self.filePositions[i + 1][0] + 1
            s += self.blankPositions[i][1] - self.blankPositions[i][0] + 1
        res = ['.' for i in range(s)]
        curr = 0
        for file in self.filePositions:
            for i in range(file[0], file[1] + 1):
                res[i] = str(curr)
            curr += 1
        return res


    def solveP1(self):
        workingS = self.modifyPositionsP1()
        res = 0
        for i, c in enumerate(workingS):
            if c == '.':
                return res
            res += i * int(c)
        return res

    def modifyPositionsP1(self):
        workingS = deepcopy(self.workingS)
        currBlank = 0
        while workingS[currBlank] != '.':
            currBlank += 1

        currChar = len(workingS) - 1
        while workingS[currChar] == '.':
            currChar -= 1

        while True:
            if currChar <= currBlank:
                break
            workingS[currBlank] = workingS[currChar]
            workingS[currChar] = '.'
            
            while workingS[currBlank] != '.':
                currBlank += 1
            while workingS[currChar] == '.':
                currChar -= 1
        return workingS

    def solveP2(self):
        workingS = self.modifyPositionsP2()
        res = 0
        for i, c in enumerate(workingS):
            if c == '.':
                continue
            res += i * int(c)
        return res

    def modifyPositionsP2(self):
        workingS = deepcopy(self.workingS)
        blanks = deepcopy(self.blankPositions)
        for currFileIndex in range(len(self.filePositions) - 1, -1, -1):
            s = self.filePositions[currFileIndex][0]
            f = self.filePositions[currFileIndex][1]
            l = f - s + 1
            for currBlank in range(len(blanks)):
                if blanks[currBlank][0] == -1:
                    continue
                if blanks[currBlank][0] > s:
                    break
                
                sb = blanks[currBlank][0]
                fb = blanks[currBlank][1]
                lb = fb - sb + 1

                if lb >= l:
                    diff = s - sb
                    for currPos in range(sb, sb + l):
                        workingS[currPos] = workingS[currPos + diff]
                        workingS[currPos + diff] = '.'
                    if lb == l:
                        blanks[currBlank][0] = -1
                    else:
                        blanks[currBlank][0] = sb + l
                    break
        return workingS

