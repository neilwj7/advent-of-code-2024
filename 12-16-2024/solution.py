from math import inf
from collections import deque
import heapq

class solution:
    def __init__(self, inputFile):
        self.grid = self.getInput(inputFile)
        self.start, self.end = self.findEndpoints()
        self.opt = {}
        self.dijkstra()

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

    def dijkstra(self):
        h = []      # (x, y, dir, score)
        seen = set()
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        heapq.heappush(h, (0, self.start[0], self.start[1], 1))

        while h:
            score, x, y, dir = heapq.heappop(h)
            self.opt[(x, y, dir)] = score
            seen.add((x, y, dir))
            dx, dy = dirs[dir]
            if (x + dx, y + dy, dir) not in seen and self.grid[x + dx][y + dy] != '#':
                heapq.heappush(h, (score + 1, x + dx, y + dy, dir))
            if (x, y, (dir + 1) % 4) not in seen: heapq.heappush(h, (score + 1000, x, y, (dir + 1) % 4))
            if (x, y, (dir - 1) % 4) not in seen: heapq.heappush(h, (score + 1000, x, y, (dir - 1) % 4))

    def solveP1(self):
        return min([self.opt[(self.end[0], self.end[1], i)] for i in range(4)])
    
    def solveP2(self):
        inPath = [[False for i in range(len(self.grid[0]))] for j in range(len(self.grid))]
        seen = set()
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        q = deque()
        for dir in range(4):
            if self.opt[(self.end[0], self.end[1], dir)] == min([self.opt[(self.end[0], self.end[1], i)] for i in range(4)]):
                q.append((self.end[0], self.end[1], dir, min([self.opt[(self.end[0], self.end[1], i)] for i in range(4)])))
                seen.add((self.end[0], self.end[1], dir))

        # backtracking bfs
        while q:
            x, y, dir, score = q.popleft()
            inPath[x][y] = True
            dx, dy = dirs[dir]
            if (x - dx, y - dy, dir) not in seen and self.opt.get((x - dx, y - dy, dir), inf) == score - 1:
                seen.add((x - dx, y - dy, dir))
                q.append((x - dx, y - dy, dir, score - 1))
            if (x, y, (dir + 1) % 4) not in seen and self.opt.get((x, y, (dir + 1) % 4), inf) == score - 1000:
                seen.add((x, y, (dir + 1) % 4))
                q.append((x, y, (dir + 1) % 4, score - 1000))
            if (x, y, (dir - 1) % 4) not in seen and self.opt.get((x, y, (dir - 1) % 4), inf) == score - 1000:
                seen.add((x, y, (dir - 1) % 4))
                q.append((x, y, (dir - 1) % 4, score - 1000))
        
        # count positions in path
        res = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if inPath[i][j]:
                    res += 1
        return res

