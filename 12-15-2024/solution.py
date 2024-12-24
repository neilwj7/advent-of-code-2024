from copy import deepcopy
class solution:
    def __init__(self, inputFile):
        self.grid, self.moves = self.getInput(inputFile)
        self.bigGrid = self.convertGrid(self.grid)

    def getInput(self, fileName):
        res1 = []
        res2 = []
        p1 = True
        with open(fileName, 'r') as file:
            for line in file:
                if line == '\n':
                    p1 = False
                elif p1:
                    line = line.strip()
                    l = []
                    for c in line:
                        l.append(c)
                    res1.append(l)
                else:
                    res2.append(line.strip())
        return res1, res2
    
    def convertGrid(self, grid):
        res = [['.' for i in range(2 * len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '.':
                    res[i][j * 2] = '.'
                    res[i][j * 2 + 1] = '.'
                elif grid[i][j] == 'O':
                    res[i][j * 2] = '['
                    res[i][j * 2 + 1] = ']'
                elif grid[i][j] == '#':
                    res[i][j * 2] = '#'
                    res[i][j * 2 + 1] = '#'
                else:
                    res[i][j * 2] = '@'
                    res[i][j * 2 + 1] = '.'
        return res

    def solveP1(self):
        grid = deepcopy(self.grid)
        i, j = self.findStart(grid)
        for commands in self.moves:
            for command in commands:
                i, j = self.performMoveP1(grid, command, i, j)
        return self.sumBoxCoords(grid)

    def myPrint(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '.':
                    print(' ', end='')
                else:
                    print(grid[i][j], end="")
            print()

    def performMoveP1(self, grid, move, i, j):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dir = 0
        if move == '>':
            dir = 1
        elif move == 'v':
            dir = 2
        elif move == '<':
            dir = 3

        if grid[i + directions[dir][0]][j + directions[dir][1]] == '.':
            grid[i][j] = '.'
            grid[i + directions[dir][0]][j + directions[dir][1]] = '@'
            return i + directions[dir][0], j + directions[dir][1]
        
        currI, currJ = i + directions[dir][0], j + directions[dir][1]
        while True:
            if grid[currI][currJ] == '#':
                return i, j
            elif grid[currI][currJ] == '.':
                grid[currI][currJ] = 'O'
                break
            currI, currJ = currI + directions[dir][0], currJ + directions[dir][1]
        grid[i + directions[dir][0]][j + directions[dir][1]] = '@'
        grid[i][j] = "."
        return i + directions[dir][0], j + directions[dir][1]

    def sumBoxCoords(self, grid):
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O' or grid[i][j] == '[':
                    res += (100 * i) + j
        return res
    
    def findStart(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    return (i, j)

    def solveP2(self):
        grid = deepcopy(self.bigGrid)
        i, j = self.findStart(grid)
        for commands in self.moves:
            for command in commands:
                ogGrid = deepcopy(grid)
                res, i, j = self.performMoveP2(grid, command, i, j)
                if not res:
                    grid = ogGrid
        return self.sumBoxCoords(grid)
    
    def performMoveP2(self, grid, move, i, j):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dir = 0
        if move == '>':
            dir = 1
        elif move == 'v':
            dir = 2
        elif move == '<':
            dir = 3

        if grid[i + directions[dir][0]][j + directions[dir][1]] == '.':
            grid[i][j] = '.'
            grid[i + directions[dir][0]][j + directions[dir][1]] = '@'
            return (True, i + directions[dir][0], j + directions[dir][1])
        
        if grid[i + directions[dir][0]][j + directions[dir][1]] == '#':
            return (False, i, j)

        if grid[i + directions[dir][0]][j + directions[dir][1]] in '[]' and dir % 2 == 0:
            s = set()
            if self.moveBoxV(grid, move, i + directions[dir][0], j + directions[dir][1], s, dir):
                grid[i][j] = '.'
                grid[i + directions[dir][0]][j + directions[dir][1]] = '@'
                return (True, i + directions[dir][0], j + directions[dir][1])
            else:
                return (False, i, j)
        
        currI, currJ = i + directions[dir][0], j + directions[dir][1]
        last = '@'
        while True:
            if grid[currI][currJ] == '#':
                return (False, i, j)
            stop = grid[currI][currJ] == '.'
            grid[currI][currJ], last = last, grid[currI][currJ]
            currI, currJ = currI + directions[dir][0], currJ + directions[dir][1]
            if stop:
                break
        
        grid[i][j] = '.'
        grid[i + directions[dir][0]][j + directions[dir][1]] = '@'
        return (True, i + directions[dir][0], j + directions[dir][1])
    
    def moveBoxV(self, grid, move, i, j, s, dir):
        if (i, j) in s:
            return True
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        res = True
        
        nextRow = i + directions[dir][0]
        if grid[i][j] == '[':
            left = j
            right = j + 1
        else:
            left = j - 1
            right = j
        s.add((i, right))
        s.add((j, left))
        
        if grid[nextRow][left] == '#' or grid[nextRow][right] == '#':
            return False
        
        if grid[nextRow][left] in '[]' and not self.moveBoxV(grid, move, nextRow, left, s, dir):
            return False
        if grid[nextRow][right] in '[]' and not self.moveBoxV(grid, move, nextRow, right, s, dir):
            return False

        grid[nextRow][left] = grid[i][left]
        grid[nextRow][right] = grid[i][right]
        grid[i][left] = '.'
        grid[i][right] = '.'

        return res
