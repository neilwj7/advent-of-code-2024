class solution:
    def __init__(self, inputFile):
        self.grid = self.getInput(inputFile)
        self.sumP2 = 0
    
    def getInput(self, fileName):
        res = []
        with open(fileName, 'r') as file:
            for line in file:
                res.append(line.strip())
        return res
    
    def sumTrailheadScoresP1(self):
        res = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '0':
                    s = set()
                    self.countScoreP1(0, i, j, s)
                    res += len(s)
        return res

    def countScoreP1(self, currLevel, i, j, s):
        if currLevel == 9:
            s.add((i, j))
            return
        if i < len(self.grid) - 1 and int(self.grid[i + 1][j]) == currLevel + 1:
            self.countScoreP1(currLevel + 1, i + 1, j, s)
        if i > 0 and int(self.grid[i - 1][j]) == currLevel + 1:
            self.countScoreP1(currLevel + 1, i - 1, j, s)
        if j < len(self.grid[0]) - 1 and int(self.grid[i][j + 1]) == currLevel + 1:
            self.countScoreP1(currLevel + 1, i, j + 1, s)
        if j > 0 and int(self.grid[i][j - 1]) == currLevel + 1:
            self.countScoreP1(currLevel + 1, i, j - 1, s)

    def sumTrailheadScoresP2(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '0':
                    self.countScoreP2(0, i, j)
        return self.sumP2

    def countScoreP2(self, currLevel, i, j):
        if currLevel == 9:
            self.sumP2 += 1
            return
        if i < len(self.grid) - 1 and int(self.grid[i + 1][j]) == currLevel + 1:
            self.countScoreP2(currLevel + 1, i + 1, j)
        if i > 0 and int(self.grid[i - 1][j]) == currLevel + 1:
            self.countScoreP2(currLevel + 1, i - 1, j)
        if j < len(self.grid[0]) - 1 and int(self.grid[i][j + 1]) == currLevel + 1:
            self.countScoreP2(currLevel + 1, i, j + 1)
        if j > 0 and int(self.grid[i][j - 1]) == currLevel + 1:
            self.countScoreP2(currLevel + 1, i, j - 1)