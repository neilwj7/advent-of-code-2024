class solution:
    def __init__(self, inputFile):
        self.original = self.getInput(inputFile)
        self.memoized = {}

    def getInput(self, fileName):
        res = []
        with open(fileName, 'r') as file:
            for line in file:
                for num in line.strip().split():
                    res.append(int(num))
        return res
    
    def solve(self, n):
        res = 0
        for num in self.original:
            res += self.recHelper(num, n)
        return res
    
    def recHelper(self, num, n):
        if (num, n) in self.memoized:
            return self.memoized[(num, n)]
        if n == 0:
            return 1
        if num == 0:
            self.memoized[(num, n)] = self.recHelper(1, n - 1)
            return self.memoized[(num, n)]
        if len(str(num)) % 2 == 0:
            return self.recHelper(int(str(num)[(len(str(num)) // 2):]), n - 1) + self.recHelper(int(str(num)[:(len(str(num)) // 2)]), n - 1)
        else:
            self.memoized[(num, n)] = self.recHelper(num * 2024, n - 1)
            return self.memoized[(num, n)]