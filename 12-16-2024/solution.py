from math import inf
from collections import deque
from copy import deepcopy

class solution:
    def __init__(self, inputFile):
        self.grid = self.getInput(inputFile)
        self.start, self.end = self.findEndpoints()
        self.endSet = set()
        self.endScore = inf
        self.Opt = [[inf for j in range(len(self.grid[0]))] for i in range(len(self.grid))]
        self.bfs()

    def getInput(self, fileName):
        res = []
        with open(fileName, 'r') as file:
            for line in file:
                res.append(line.strip())
        return res
    
    def findEndpoints(self):
        res = [(0, 0), (0, 0)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 'S':
                    res[0] = (i, j)
                if self.grid[i][j] == 'E':
                    res[1] = (i, j)
        return res
    
    def myPrint(self, s):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if (i, j) in s:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()

    def solveP1(self):
        return self.endScore

    def solveP2(self):
        return len(self.endSet)
    
    def bfs(self):
        q = deque()     # (i, j, dir, score, setOfPath)
        #self.responsibleFor[(self.start[0], self.start[1])].add((self.start[0], self.start[1]))
        startingset = set()
        q.append((self.start[0], self.start[1], 1, 0))
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while len(q) != 0:
            i, j, dir, score = q.popleft()
            #print(f"({i}, {j})")
            # if (i, j) in s:
            #     continue
            # if self.Opt[i][j] + 1000 < score or self.endScore < score:
            #     continue

            self.Opt[i][j] = min(score, self.Opt[i][j])
            #s.add((i, j))

            if (i, j) == (self.end[0], self.end[1]):
                if score < self.endScore:
                    #print(f"new end score: {score}")
                    self.endScore = score
                    #self.endSet = s
                elif (score == self.endScore):
                    #self.endSet = self.endSet | s
                    pass
                continue

            # same direction
            dy, dx = directions[dir]
            if self.grid[i + dy][j + dx] != '#':
                #newS = deepcopy(s)
                q.append((i + dy, j + dx, dir, score + 1))
            
            # one up
            dy, dx = directions[(dir + 1) % 4]
            if self.grid[i + dy][j + dx] != '#':
                #newS = deepcopy(s)
                q.append((i + dy, j + dx, (dir + 1) % 4, score + 1001))

            # one down
            dy, dx = directions[(dir - 1) % 4]
            if self.grid[i + dy][j + dx] != '#':
                #newS = deepcopy(s)
                q.append((i + dy, j + dx, (dir - 1) % 4, score + 1001))
        return 