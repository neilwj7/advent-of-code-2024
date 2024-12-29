class solution:
    def __init__(self, inputFile):
        self.available, self.targets = self.getInput(inputFile)

    def getInput(self, fileName):
        with open(fileName, 'r') as file:
            res1 = []
            res2 = []
            for line in file:
                if len(res1) == 0:
                    res1 = line.strip().replace(',', '').split()
                    continue
                if line == '\n':
                    continue
                res2.append(line.strip())
            return set(res1), res2

    def solveP1(self):
        res = 0
        for s in self.targets:
            if self.possible(s): res += 1
        return res
    
    def solveP2(self):
        res = 0
        for s in self.targets:
            res += self.possible(s)
        return res
    
    def possible(self, s):
        Opt = [0 for _ in range(len(s) + 1)]
        Opt[len(s)] = 1
        if s[:1] in self.available: Opt[0] = 1
        for i in range(1, len(s)):
            for j in range(-1, i + 1):
                if Opt[j] and s[j + 1:i+1] in self.available:
                    Opt[i] += Opt[j]
        return Opt[len(s) - 1]
