from collections import deque
class solution:
    def __init__(self, dimension, inputFile):
        self.points = self.getInput(inputFile)
        self.dims = dimension
    
    def getInput(self, fileName):
        res = []
        with open(fileName, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                res.append((int(parts[0]), int(parts[1])))
        return res
    
    def solveP1(self, numBytes):
        obstacles = set(self.points[:numBytes])
        q = deque()
        seen = set()

        q.append((0, 0, 0))
        seen.add((0, 0))
        while q:
            x, y, i = q.popleft()

            if (x, y) == (self.dims - 1, self.dims - 1):
                return i
            
            if x - 1 != -1 and (x - 1, y) not in seen and (x - 1, y) not in obstacles:
                seen.add((x - 1, y))
                q.append((x - 1, y, i + 1))
            
            if x + 1 != self.dims and (x + 1, y) not in seen and (x + 1, y) not in obstacles:
                seen.add((x + 1, y))
                q.append((x + 1, y, i + 1))
            
            if y - 1 != -1 and (x, y - 1) not in seen and (x, y - 1) not in obstacles:
                seen.add((x, y - 1))
                q.append((x, y - 1, i + 1))
            
            if y + 1 != self.dims and (x, y + 1) not in seen and (x, y + 1) not in obstacles:
                seen.add((x, y + 1))
                q.append((x, y + 1, i + 1))

        return -1

    def solveP2(self):
        for i in range(1024, 3450):
            if self.solveP1(i) == -1:
                return self.points[i - 1]
        return (-1, -1)