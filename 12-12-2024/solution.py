class solution:
    def __init__(self, inputFile):
        self.grid = self.getInput(inputFile)

    def getInput(self, fileName):
        res = []
        with open(fileName, 'r') as file:
            for line in file:
                res.append(line.strip())
        return res
    
    def countFenceCostTotalP1(self):
        plotCovered = [[0 for i in range(len(self.grid))] for j in range(len(self.grid))]
        res = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                res += self.countCostOfFenceP1(i, j, plotCovered)
        return res
    
    def countFenceCostTotalP2(self):
        plotCovered = [[0 for i in range(len(self.grid))] for j in range(len(self.grid))]
        res = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                res += self.countCostOfFenceP2(i, j, plotCovered)
        return res
    
    def countCostOfFenceP1(self, i, j, plotCovered):
        if plotCovered[i][j] == 1:
            return 0
        # first we must find section: represented as a set of tuples of each position in the section
        s = set()
        self.findSection(i, j, plotCovered, s)
        res = 0
        for currI, currJ in s:
            if (currI + 1, currJ) not in s:
                res += len(s)
            if (currI - 1, currJ) not in s:
                res += len(s)
            if (currI, currJ - 1) not in s:
                res += len(s)
            if (currI, currJ + 1) not in s:
                res += len(s)
        return res
    
    def countCostOfFenceP2(self, i, j, plotCovered):
        if plotCovered[i][j] == 1:
            return 0
        # first we must find section: represented as a set of tuples of each position in the section
        s = set()
        self.findSection(i, j, plotCovered, s)
        sides = 0
        for currI, currJ in s:
            if (currI - 1, currJ) not in s and ((currI, currJ - 1) not in s or (currI - 1, currJ - 1) in s):
                sides += 1
            if (currI + 1, currJ) not in s and ((currI, currJ + 1) not in s or (currI + 1, currJ + 1) in s):
                sides += 1
            if (currI, currJ - 1) not in s and ((currI + 1, currJ) not in s or (currI + 1, currJ - 1) in s):
                sides += 1
            if (currI, currJ + 1) not in s and ((currI - 1, currJ) not in s or (currI - 1, currJ + 1) in s):
                sides += 1
        return sides * len(s)
    
    def findSection(self, i, j, plotCovered, s):
        s.add((i, j))
        plotCovered[i][j] = 1
        plant = self.grid[i][j]
        if i > 0 and plotCovered[i - 1][j] == 0 and self.grid[i - 1][j] == plant:
            self.findSection(i - 1, j, plotCovered, s)
        if j > 0 and plotCovered[i][j - 1] == 0 and self.grid[i][j - 1] == plant:
            self.findSection(i, j - 1, plotCovered, s)
        if i < len(self.grid) - 1 and plotCovered[i + 1][j] == 0 and self.grid[i + 1][j] == plant:
            self.findSection(i + 1, j, plotCovered, s)
        if j < len(self.grid) - 1 and plotCovered[i][j + 1] == 0 and self.grid[i][j + 1] == plant:
            self.findSection(i, j + 1, plotCovered, s)