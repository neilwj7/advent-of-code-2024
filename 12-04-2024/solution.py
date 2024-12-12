class solution:
    def __init__(self, fileName):
        self.grid = self.getInput(fileName)


    def getInput(self, fileName):
        res = []
        with open(fileName, 'r') as file:
            for line in file:
                res.append(line)
        return res


    def countXmas(self):
        res = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 'X':
                    res += self.tryXmas(i, j)
        return res
    

    def tryXmas(self, i, j):
        res = 0

        # west
        try:
            if j < 3:
                pass
            elif self.grid[i][j - 1] == 'M' and self.grid[i][j - 2] == 'A' and self.grid[i][j - 3] == 'S':
                res += 1
        except:
            pass

        # northwest
        try:
            if i < 3 or j < 3:
                pass
            elif self.grid[i - 1][j - 1] == 'M' and self.grid[i - 2][j - 2] == 'A' and self.grid[i - 3][j - 3] == 'S':
                res += 1
        except:
            pass

        # north
        try:
            if i < 3:
                pass
            elif self.grid[i - 1][j] == 'M' and self.grid[i - 2][j] == 'A' and self.grid[i - 3][j] == 'S':
                res += 1
        except:
            pass

        # northeast
        try:
            if i < 3:
                pass
            elif self.grid[i - 1][j + 1] == 'M' and self.grid[i - 2][j + 2] == 'A' and self.grid[i - 3][j + 3] == 'S':
                res += 1
        except:
            pass

        # east
        try:
            if self.grid[i][j + 1] == 'M' and self.grid[i][j + 2] == 'A' and self.grid[i][j + 3] == 'S':
                res += 1
        except:
            pass

        # southeast
        try:
            if self.grid[i + 1][j + 1] == 'M' and self.grid[i + 2][j + 2] == 'A' and self.grid[i + 3][j + 3] == 'S':
                res += 1
        except:
            pass

        # south
        try:
            if self.grid[i + 1][j] == 'M' and self.grid[i + 2][j] == 'A' and self.grid[i + 3][j] == 'S':
                res += 1
        except:
            pass

        # southwest
        try:
            if j < 3:
                pass
            elif self.grid[i + 1][j - 1] == 'M' and self.grid[i + 2][j - 2] == 'A' and self.grid[i + 3][j - 3] == 'S':
                res += 1
        except:
            pass
        return res
    
    
    def countXmasCross(self):
        res = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 'A':
                    if self.tryXmasCross(i, j):
                        res += 1
        return res


    def tryXmasCross(self, i, j):
        if i < 1 or j < 1:
            return False
        try:
            if self.grid[i + 1][j - 1] == 'M' and self.grid[i - 1][j + 1] == 'S':
                if self.grid[i - 1][j - 1] == 'M' and self.grid[i + 1][j + 1] == 'S':
                    return True
                if self.grid[i - 1][j - 1] == 'S' and self.grid[i + 1][j + 1] == 'M':
                    return True
            if self.grid[i + 1][j - 1] == 'S' and self.grid[i - 1][j + 1] == 'M':
                if self.grid[i - 1][j - 1] == 'M' and self.grid[i + 1][j + 1] == 'S':
                    return True
                if self.grid[i - 1][j - 1] == 'S' and self.grid[i + 1][j + 1] == 'M':
                    return True
        except:
            return False
