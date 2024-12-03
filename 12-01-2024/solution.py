class solution:
    def __init__(self, file):
        self.input = file

    def distance(self):
        a, b = self.getArrays(self.input)

        a.sort()
        b.sort()

        res = 0
        for i in range(len(a)):
            res += abs(a[i] - b[i])
        return res
    def similarity(self):
        a, b = self.getArrays(self.input)

        a.sort()
        b.sort()

        # turn b into a map
        bMap = {}

        i = 0
        while i < len(b):
            currNum = b[i]
            bMap[currNum] = 1
            if i == len(b) - 1:
                break
            i += 1
            while b[i] == currNum:
                i += 1
                bMap[currNum] += 1
                if i == len(b) - 1:
                    break

        res = 0
        for i in range(len(a)):
            res += (a[i] * bMap.get(a[i], 0))
        return res
    
    def getArrays(self, file):
        a, b = [], []
        with open(file, 'r') as openFile:
            for line in openFile:
                twoNumbers = line.split()
                a.append(int(twoNumbers[0]))
                b.append(int(twoNumbers[1]))
        return (a, b)
