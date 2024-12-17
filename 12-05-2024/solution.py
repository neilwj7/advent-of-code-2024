from collections import defaultdict
class solution:
    def __init__(self, inputFile):
        self.orderDict, self.updates = self.readFromFile(inputFile)

    def readFromFile(self, inputFile):
        input1 = []
        input2 = []
        midpointflag = False
        with open(inputFile, 'r') as file:
            for line in file:
                if line == '\n':
                        midpointflag = True
                        continue
                if midpointflag:
                    input2.append(line)
                else:
                    input1.append(line)
        res2 = [list(map(int, line.strip().split(','))) for line in input2]
        res1 = defaultdict(list)
        for line in input1:
            line = line.strip()
            num1, num2 = map(int, line.split('|'))
            res1[num2].append(num1)
        return [res1, res2]
    
    def sumValidUpdates(self):
        res = 0
        for update in self.updates:
            if self.isValidUpdate(update):
                res += update[len(update) // 2]
        return res
    
    def isValidUpdate(self, update):
        redoFlag = True
        res = True
        while redoFlag:
            redoFlag = False
            for i in range(len(update)):
                for j in range(i):
                    if update[i] in self.orderDict[update[j]]:
                        update[i], update[j] = update[j], update[i]
                        redoFlag = True
                        res = False
                        break
                if redoFlag:
                    break
        return res
    
    def sumInvalidUpdates(self):
        res = 0
        for update in self.updates:
            if not self.isValidUpdate(update):
                res += update[len(update) // 2]
        return res