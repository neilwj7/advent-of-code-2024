class solution:
    def __init__(self, inputFile):
        self.computers, self.connections = self.getInput(inputFile)

    def getInput(self, fileName):
        connections = set()
        computers = []
        seenComputers = set()
        with open(fileName, 'r') as file:
            for line in file:
                c1, c2 = line[:2], line[3:5]
                if c1 not in seenComputers: computers.append(c1)
                if c2 not in seenComputers: computers.append(c2)
                for c in [c1, c2]: seenComputers.add(c) 
                connections.add((c1, c2))
        return computers, connections

    def solveP1(self):
        sets = self.findParties(self.connections, 2)
        res = 0
        for s in sets:
            if s[0][0] == 't' or s[1][0] == 't' or s[2][0] == 't': res += 1
        return res
        
    def solveP2(self):
        s = self.connections
        n = 2
        while True:
            newS = self.findParties(s, n)
            if len(newS) == 1:
                for p in newS:
                    return sorted([c for c in p])
            s, n = newS, n + 1

    def findParties(self, parties, n):
        res = set()
        for party in parties:
            for c in self.computers:
                for x in party:
                    if not ((x, c) in self.connections or (c, x) in self.connections):
                        break
                else:
                    res.add(tuple(sorted(list(party) + [c])))
        return res