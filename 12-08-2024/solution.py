from math import isclose
from collections import defaultdict
class solution:
    def __init__(self, inputFile):
        self.grid = self.getInput(inputFile)
        self.map = self.createDict()
        self.marked = [['0' for i in range(len(self.grid[0]))] for j in range(len(self.grid))]
    
    def getInput(self, fileName):
        res = []
        with open(fileName, 'r') as file:
            for line in file:
                res.append(line.strip())
        return res
    
    def createDict(self):
        res = defaultdict(list)
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                if self.grid[x][y] != '.':
                    res[str(self.grid[x][y])].append([x, y])
        return res
    
    def countAntinodePositions(self):
        for key in self.map:
            l = self.map[key]
            for i in range(len(l) - 1):
                for j in range(i + 1, len(l)):
                    self.markLine(l[i], l[j])
        return self.countMarkedLocations()
    
    def countAntinodePositionsPt2(self):
        for key in self.map:
            l = self.map[key]
            for i in range(len(l) - 1):
                for j in range(i + 1, len(l)):
                    self.markLinePt2(l[i], l[j])
        return self.countMarkedLocations()
    
    def markLine(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        newX, newY = x2 + (x2 - x1), y2 + (y2 - y1)
        if 0 <= newX and newX < len(self.grid) and 0 <= newY and newY < len(self.grid[0]):
            self.marked[newX][newY] = '1'
        newX, newY = x1 - (x2 - x1), y1 - (y2 - y1)
        if 0 <= newX and newX < len(self.grid) and 0 <= newY and newY < len(self.grid[0]):
            self.marked[newX][newY] = '1'
    
    def markLinePt2(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        if x1 == x2:    # infinite slope
            for y in range(len(self.grid[x1])):
                self.marked[x1][y] = '1'
            return
        m = (y2 - y1) / (x2 - x1)   # slope = rise / run
        b = y2 - (m * x2)   # solve for y-intercept
        for x in range(len(self.grid)):
            y = (m * x) + b
            if isclose(y, round(y), abs_tol=1e-6) and 0 <= y and y < len(self.grid[0]):
                self.marked[x][round(y)] = '1'

    def countMarkedLocations(self):
        res = 0
        for i in range(len(self.marked)):
            for j in range(len(self.marked[i])):
                if self.marked[i][j] == '1':
                    res += 1
        return res
