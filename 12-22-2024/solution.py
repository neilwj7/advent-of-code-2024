from copy import deepcopy
from collections import deque
class solution:
    def __init__(self, inputFile):
        self.prices = self.getInput(inputFile)
    
    def getInput(self, fileName):
        with open(fileName, 'r') as file: return [int(line.strip()) for line in file]

    def solveP1(self):
        prices = deepcopy(self.prices)
        for _ in range(2000): self.update(prices)
        return sum(prices)
    
    def solveP2(self):
        prices = deepcopy(self.prices)
        candidateMap = [{} for i in range(10)]
        res = 0
        for i in range(len(prices)):
            q = deque()
            lp = prices[i] % 10
            seenSequences = set()
            for _ in range(2000):
                prices[i] = self.singleUpdate(prices[i])
                np = prices[i] % 10
                dp = np - lp
                q.append(dp)
                if len(q) == 5: q.popleft()
                if len(q) == 4: 
                    if tuple(q) in seenSequences: 
                        lp = np
                        continue
                    else: seenSequences.add(tuple(q))
                    candidateMap[np][tuple(q)] = candidateMap[np].get(tuple(q), 0) + 1
                    total = 0
                    for j in range(0, 10):
                        if tuple(q) in candidateMap[j]: total += candidateMap[j][tuple(q)] * j
                    res = max(total, res)
                lp = np
        return res

    def singleUpdate(self, num):
        # part 1
        n = num << 6
        num = num ^ n
        num = num & (2 ** 24 - 1)

        # part 2
        n = num >> 5
        num = num ^ n
        num = num & (2 ** 24 - 1)

        # part 3
        n = num << 11
        num = num ^ n
        return num & (2 ** 24 - 1)
    
    def update(self, prices):
        for i in range(len(prices)):
            prices[i] = self.singleUpdate(prices[i])