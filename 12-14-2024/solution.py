from copy import deepcopy
class solution:
    def __init__(self, inputFile, width, length):
        self.robots = self.getInput(inputFile)
        self.width = width
        self.length = length
    
    def getInput(self, fileName):
        with open(fileName, 'r') as file:
            res = []
            for line in file:
                parts = line.strip().split(' ')
                curr = [-1 for i in range(4)]
                parts[0] = parts[0][2:]
                parts[1] = parts[1][2:]
                parts = parts[0].split(',') + parts[1].split(',')
                for i, part in enumerate(parts):
                    curr[i] = int(part)
                res.append(curr)
            return res
        
    def solveP1(self):
        temp = deepcopy(self.robots)
        self.simulate(temp, 100)
        return self.findSafetyFactor(temp)
    
    def simulate(self, robots, times):
        for i in range(len(robots)):
            robots[i][0] = (robots[i][0] + (times * robots[i][2])) % self.width
            robots[i][1] = (robots[i][1] + (times * robots[i][3])) % self.length

    def findSafetyFactor(self, robots):
        q1, q2, q3, q4 = 0, 0, 0, 0
        midlineW, midlineL = (self.width - 1) // 2, (self.length - 1) // 2
        for robot in robots:
            if robot[0] < midlineW and robot[1] < midlineL:
                q1 += 1
            if robot[0] > midlineW and robot[1] < midlineL:
                q2 += 1
            if robot[0] > midlineW and robot[1] > midlineL:
                q3 += 1
            if robot[0] < midlineW and robot[1] > midlineL:
                q4 += 1
        return q1 * q2 * q3 * q4
    
    def solveP2(self):
        robots = deepcopy(self.robots)
        # create the grid
        grid = [[0 for i in range(self.width)] for j in range(self.length)]
        
        # populate the grid with robots
        for robot in robots:
            grid[robot[1]][robot[0]] += 1
        
        # keep running simulations until found
        res = 0
        while True:
            # update count
            res += 1

            # move robots once
            for robot in robots:
                grid[robot[1]][robot[0]] -= 1
                robot[0] = (robot[0] + robot[2]) % self.width
                robot[1] = (robot[1] + robot[3]) % self.length
                grid[robot[1]][robot[0]] += 1
        
            # check for pattern
            curr = self.findSafetyFactor(robots)
            if curr > 260000000 or curr < 160000000:
                self.myPrint(grid)
                break
        return res
    
    def myPrint(self, grid):
        for i in range(len(grid)):
            print('[', end="")
            for j in range(len(grid[0])):
                if grid[i][j]:
                    print('#', end="")
                else:
                    print(' ', end="")
            print(']')