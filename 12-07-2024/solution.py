class solution:
    def __init__(self, inputFile):
        self.targets, self.sequences = self.getInput(inputFile)
    
    def getInput(self, fileName):
        targets = []
        sequences = []
        with open(fileName, 'r') as file:
            for line in file:
                parts = line.split()
                targets.append(int(parts[0].strip(':')))
                curr = []
                for i in range(1, len(parts)):
                    curr.append(int(parts[i]))
                sequences.append(curr)
        return targets, sequences
    
    def countTotalCalibration(self):
        res = 0
        for i in range(len(self.targets)):
            if self.check(self.targets[i], self.sequences[i]):
                res += self.targets[i]
        return res
    
    def countTotalCalibrationWithConcat(self):
        res = 0
        for i in range(len(self.targets)):
            if self.checkWithConcat(self.targets[i], self.sequences[i]):
                res += self.targets[i]
        return res
    
    def check(self, target, values):
        # base case
        if len(values) == 1:
            if values[0] == target:
                return True
            else:
                return False
        if len(values) == 2:
            return self.check(target, [values[0] + values[1]]) or self.check(target, [values[0] * values[1]])
        return self.check(target, [values[0] + values[1]] + values[2:]) or self.check(target, [values[0] * values[1]] + values[2:])
        
    def checkWithConcat(self, target, values):
        # base case
        if len(values) == 1:
            if values[0] == target:
                return True
            else:
                return False
        if len(values) == 2:
            return self.checkWithConcat(target, [values[0] + values[1]]) or self.checkWithConcat(target, [values[0] * values[1]]) or self.checkWithConcat(target, [int(str(values[0]) + str(values[1]))])
        return self.checkWithConcat(target, [values[0] + values[1]] + values[2:]) or self.checkWithConcat(target, [values[0] * values[1]] + values[2:]) or self.checkWithConcat(target, [int(str(values[0]) + str(values[1]))] + values[2:])