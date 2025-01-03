class solution:
    def __init__(self, fileName):
        self.s = self.getInput(fileName)
        self.enable = True

    def getInput(self, fileName):
        res = ""
        with open(fileName, 'r') as file:
            for line in file:
                res = res + line
        return res

    def solveP1(self):
        res = 0
        for i in range(len(self.s)):
            res += self.checkMul(i)
        return res

    def solveP2(self):
        res = 0
        for i in range(len(self.s)):
            self.enable = self.updateEnable(i)
            if self.enable:
                res += self.checkMul(i)
        return res

    def updateEnable(self, i):
        if len(self.s) - i < 4:
            return self.enable
        if self.s[i:i+4] == 'do()':
            return True
        if len(self.s) - i < 7:
            return self.enable
        if self.s[i:i+7] == "don't()":
            return False
        return self.enable

    def checkMul(self, i):
        # first check if substring starts with 'mul('
        if (len(self.s) - i < 4) or (self.s[i:i+4] != 'mul('): return 0

        i += 4
        if i >= len(self.s) - 1: return 0
        
        # check first number
        firstNum = ''
        curr = self.s[i]
        while True:
            if curr == ',':
                if firstNum != '':
                    firstNum = int(firstNum)
                    break
                else:
                    return 0
            elif curr.isdigit():
                firstNum = firstNum + curr
            else:
                return 0
            i += 1
            if i == len(self.s):
                return 0
            curr = self.s[i]
        
        # if we get here, we have a valid first number and i is currently at the comma
        # check second number
        i += 1
        if i >= len(self.s) - 1:
            return 0
        secondNum = ''
        curr = self.s[i]
        while True:
            if curr == ')':
                if secondNum != '':
                    secondNum = int(secondNum)
                    break
                else:
                    return 0
            elif curr.isdigit():
                secondNum = secondNum + curr
            else:
                return 0
            i += 1
            if i == len(self.s):
                return 0
            curr = self.s[i]
        
        # if we get here, we have two valid numbers and a valid mul call
        return firstNum * secondNum