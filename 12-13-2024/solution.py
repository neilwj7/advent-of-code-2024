from copy import deepcopy
class solution:
    def __init__(self, inputFile):
        self.map = self.getInput(inputFile)
    
    def getInput(self, fileName):
        res = []
        curr = {}
        with open(fileName, 'r') as file:
            for line in file:
                line = line.strip()
                if line == '':
                    res.append(curr)
                    curr = {}
                elif len(curr) == 0:
                    parts = line[12:].split(',')
                    curr['a'] = (int(parts[0]), int(parts[1][3:]))
                elif len(curr) == 1:
                    parts = line[12:].split(',')
                    curr['b'] = (int(parts[0]), int(parts[1][3:]))
                else:
                    parts = line[9:].split(',')
                    curr['p'] = (int(parts[0]), int(parts[1][3:]))
            res.append(curr)
        return res
    
    def solve(self, add):
        newMap = self.convertMap(add)
        res = 0
        for d in newMap:
            a = d['a']
            b = d['b']
            p = d['p']
            temp = ((b[1])*(a[0])-(a[1])*(b[0]))
            if temp != 0:
                y = round(((a[0])*(p[1])-(a[1])*(p[0])) / temp)
                x = round((p[0] - (b[0] * y)) / a[0])
            else:
                continue
            if x >= 0 and y >= 0 and x * a[0] + y * b[0] == p[0] and x * a[1] + y * b[1] == p[1]:
                res += x * 3 + y
        return res
    
    def convertMap(self, add):
        res = deepcopy(self.map)
        for d in res:
            d['p'] = tuple([list(d['p'])[0] + add, list(d['p'])[1] + add])
        return res