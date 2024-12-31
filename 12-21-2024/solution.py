from itertools import product
from functools import cache
from collections import deque, defaultdict
class solution:
    def __init__(self, inputFile):
        self.sequences = self.getInput(inputFile)
        self.numKeypad = [['7', '8', '9'], 
                          ['4', '5', '6'], 
                          ['1', '2', '3'] ,
                          [None, '0', 'A']]
        
        self.moveKeypad = [[None, '^', 'A'], 
                           ['<', 'v', '>']]
        self.sequencesMoveKeypad = self.getSequences(self.moveKeypad)
    
    def getInput(self, fileName):
        with open(fileName, 'r') as file:
            return [line.strip() for line in file.read().splitlines()]
   
    def solveP1(self):
        res = 0
        for code in self.sequences:
            inputs = self.solve(code, self.numKeypad)
            optimal = float('inf')
            for input in inputs:
                total = 0
                for x, y in zip('A' + input, input):
                    total += self.getLength(x, y, 2)
                optimal = min(optimal, total)
            res += optimal * int(code[:3])
        return res
    
    def solveP2(self):
        res = 0
        for code in self.sequences:
            inputs = self.solve(code, self.numKeypad)
            optimal = float('inf')
            for input in inputs:
                total = 0
                for x, y in zip('A' + input, input):
                    total += self.getLength(x, y)
                optimal = min(optimal, total)
            res += optimal * int(code[:3])
        return res
    
    # take a code and a keypad and calculate all shortest path commands (ex: ^<A>...)
    def solve(self, code, keypad):
        # first find position of each key in the current keypad
        sequences = self.getSequences(keypad)
        options = [sequences[(x, y)] for x, y in zip('A' + code, code)]
        return list(''.join(x) for x in product(*options))
    
    @cache
    def getLength(self, x, y, depth=25):
        if depth == 1:
            return len(self.sequencesMoveKeypad[(x, y)][0])

        optimal = float('inf')
        for sequence in self.sequencesMoveKeypad[(x, y)]:
            length = 0
            for i, j in zip('A' + sequence, sequence):
                length += self.getLength(i, j, depth - 1)
            optimal = min(optimal, length)
        return optimal

    def getSequences(self, keypad):
        # first find position of each key in the current keypad
        positions = {}
        for i in range(len(keypad)):
            for j in range(len(keypad[i])):
                if keypad[i][j] != None: positions[keypad[i][j]] = (i, j)
        
        # find shortest combinations for each pair of two keys
        sequences = defaultdict(list)
        for pos1 in positions:
            for pos2 in positions:
                if pos1 == pos2: sequences[(pos1, pos2)] = ['A']
                else:
                    # do bfs to find all shortest paths
                    optimal = float('inf')
                    q = deque()
                    q.append(((positions[pos1], positions[pos2]), 0, ''))
                    while q:
                        ((cx, cy), (tx, ty)), score, path = q.popleft()
                        if cx == tx and cy == ty: 
                            if score > optimal: break
                            optimal = score
                            sequences[(pos1, pos2)].append(path + 'A')
                        for nx, ny, np in [[cx + 1, cy, path + 'v'], [cx - 1, cy, path + '^'], [cx, cy + 1, path + '>'], [cx, cy - 1, path + '<']]:
                            if not (0 <= nx < len(keypad) and 0 <= ny < len(keypad[nx])) or keypad[nx][ny] == None: continue
                            else: q.append((((nx, ny), (tx, ty)), score + 1, np))
        return sequences
