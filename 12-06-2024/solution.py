class solution:
    def __init__(self, fileName):
        self.grid = self.getInput(fileName)
        self.markedLocations = [['0' for i in range(len(self.grid[0]))] for j in range(len(self.grid))]
        self.start = self.getInitialCoords()
        if self.grid[self.start[0]][self.start[1]] == '^': self.initialDir = 0
        elif self.grid[self.start[0]][self.start[1]] == '>': self.initialDir = 1
        elif self.grid[self.start[0]][self.start[1]] == 'v': self.initialDir = 2
        else: self.initialDir = 3

    def getInput(self, fileName):
        res = []
        with open(fileName, 'r') as file:
            for line in file:
                res.append(line.strip())
        return res

    def markDistinctSquares(self):
        curr = self.start
        self.markedLocations[curr[0]][curr[1]] = '1'
        dir = self.initialDir
        directions = [[-1,0], [0, 1], [1, 0], [0, -1]]
        while True:
            if curr[0] + directions[dir][0] >= len(self.grid) or curr[0] + directions[dir][0] < 0 or curr[1] + directions[dir][1] >= len(self.grid[0]) or curr[1] + directions[dir][1] < 0:
                return
            else:
                if self.grid[curr[0] + directions[dir][0]][curr[1] + directions[dir][1]] == '#':
                    dir = (dir + 1) % 4
                else:
                    curr = [curr[0] + directions[dir][0], curr[1] + directions[dir][1]]
                    self.markedLocations[curr[0]][curr[1]] = '1'
    
    def countDistinctSquares(self):
        self.markDistinctSquares()
        res = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.markedLocations[i][j] == '1':
                    res += 1
        return res
    
    def countLoopAdds(self):
        self.markDistinctSquares()
        res = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if i == self.start[0] and j == self.start[1]:
                    continue
                if self.markedLocations[i][j] != '1':
                    continue
                if self.checkLoopWithAdd(i, j):
                    res += 1
        return res

    def checkLoopWithAdd(self, i, j):
        curr = self.start
        dir = self.initialDir
        directions = [[-1,0], [0, 1], [1, 0], [0, -1]]
        for _ in range(len(self.grid) * len(self.grid[0])):
            if curr[0] + directions[dir][0] >= len(self.grid) or curr[0] + directions[dir][0] < 0 or curr[1] + directions[dir][1] >= len(self.grid[0]) or curr[1] + directions[dir][1] < 0:
                return False
            else:
                if self.grid[curr[0] + directions[dir][0]][curr[1] + directions[dir][1]] == '#' or (curr[0] + directions[dir][0] == i and curr[1] + directions[dir][1] == j):
                    dir = (dir + 1) % 4
                else:
                    curr = [curr[0] + directions[dir][0], curr[1] + directions[dir][1]]
        return True

    def getInitialCoords(self):
        checkFor = ['^','v','>','<']
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] in checkFor:
                    return [i, j]
