class solution:
    def __init__(self, inputFile):
        self.grids, self.locks, self.keys = self.getInput(inputFile)
    
    def getInput(self, fileName):
        grids, locks, keys = [], [], []
        # first find raw grids
        with open(fileName, 'r') as file:
            curr = []
            for line in file: 
                if line == '\n': 
                    grids.append(curr)
                    curr = []
                else: curr.append(line.strip())
            grids.append(curr)

        # convert to pin heights for both keys and locks
        for grid in grids:
            curr = [0 for i in range(len(grid[0]))]
            if grid[0][0] == '#':   # locks
                for row in range(1, len(grid)):
                    for col in range(len(grid[row])):
                        if grid[row][col] == '#': curr[col] = row
                locks.append(curr)
            else:
                for row in range(len(grid) - 2, 0, -1):
                    for col in range(len(grid[row])):
                        if grid[row][col] == '#': curr[col] = len(grid) - row - 1
                keys.append(curr)
        
        # return all data
        return grids, locks, keys
    
    def solveP1(self):
        res = 0
        # check every key against every lock
        for key in self.keys:
            for lock in self.locks:
                if self.noOverlap(key, lock, len(self.grids[0]) - 2): res += 1
        return res
    
    def noOverlap(self, key, lock, threshold):
        for i in range(len(key)):
            if key[i] + lock[i] > threshold: return False
        return True