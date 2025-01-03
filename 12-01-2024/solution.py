class solution:
    def __init__(self, inputFile):
        self.a, self.b = self.getInput(inputFile)

    def distance(self):
        self.a.sort()
        self.b.sort()
        res = 0
        for i in range(len(a)):
            res += abs(self.a[i] - self.b[i])
        return res

    def similarity(self):
        # turn b into a map
        bMap = {}
        for num in b:
            bMap[num] = bMap.get(num, 0) + 1

        # count similarity score
        res = 0
        for i in range(len(a)):
            res += (a[i] * bMap.get(a[i], 0))
        return res

    def getArrays(self, fileName):
        a, b = [], []
        with open(fileName, 'r') as openFile:
            for line in openFile:
                twoNumbers = line.split()
                a.append(int(twoNumbers[0]))
                b.append(int(twoNumbers[1]))
        return (a, b)
