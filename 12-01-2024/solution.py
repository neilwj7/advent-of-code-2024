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

        # turn b into a map
        bMap = {}
        for num in b:
            bMap[num] = bMap.get(num, 0) + 1

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
