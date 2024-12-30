class solution:
    def __init__(self, inputFile):
        self.grid = self.getInput(inputFile)
        self.start, self.end = self.findEndpoints()

    def getInput(self, fileName):
        res = []
        with open(fileName, 'r') as file:
            for line in file: res.append(line.strip())
        return res

    def findEndpoints(self):
        res = [(-1, -1), (-1, -1)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 'S': res[0] = (i, j)
                if self.grid[i][j] == 'E': res[1] = (i, j)
        return res

    def findPath(self):
        res = []
        s = set()
        curr = (self.start[0], self.start[1])
        while True:
            res.append(curr)
            if curr == self.end: break
            s.add((curr[0], curr[1]))
            if curr[0] != 0 and self.grid[curr[0] - 1][curr[1]] != '#' and (curr[0] - 1, curr[1]) not in s: curr = (curr[0] - 1, curr[1])
            elif curr[1] != 0 and self.grid[curr[0]][curr[1] - 1] != '#' and (curr[0], curr[1] - 1) not in s: curr = (curr[0], curr[1] - 1)
            elif curr[0] != len(self.grid) - 1 and self.grid[curr[0] + 1][curr[1]] != '#' and (curr[0] + 1, curr[1]) not in s: curr = (curr[0] + 1, curr[1])
            else: curr = (curr[0], curr[1] + 1)
        return res

    def solve(self, threshold, time):
        path = self.findPath()
        res = 0
        for i in range(len(path)):
            for j in range(i, len(path)):
                dx, dy = abs(path[j][0] - path[i][0]), abs(path[j][1] - path[i][1])
                if dx + dy <= time and j - i > (dx + dy):
                    if j - (i + dx + dy) >= threshold:
                        res += 1
        return res