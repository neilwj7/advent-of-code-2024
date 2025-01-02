from collections import deque
class solution:
    def __init__(self, inputFile):
        self.states, self.gates = self.getInput(inputFile)
    
    def getInput(self, fileName):
        states, gates, halfwayFlag = {}, [], False
        with open(fileName, 'r') as file:
            for line in file:
                if line == '\n': halfwayFlag = True
                elif not halfwayFlag: states[line[:3]] = int(line[5:6])
                else: gates.append([part for part in line.strip().split()])
        for gate in gates:
            del gate[3]
        return states, gates

    def solveP1(self):
        q = deque(self.gates)
        while q:
            x, op, y, z = q.popleft()
            if x in self.states and y in self.states:
                self.states[z] = self.evaluate(x, op, y)
            else: q.append([x, op, y, z])
        
        number = []
        for key in sorted(list(self.states)):
            if key[0] == 'z': number.append(self.states[key])
        
        res = 0
        for n, bit in enumerate(number):
            if bit: res += (2 ** n)
        return res

    def evaluate(self, x, op, y):
        if op == 'AND': return int(self.states[x] and self.states[y])
        if op == 'OR': return int(self.states[x] or self.states[y])
        else: return int((self.states[x] and not self.states[y]) or (not self.states[x] and self.states[y]))

    def searchForVariables(self):
        res = [['none', 'none'] for i in range(45)]
        for x, op, y, z in self.gates:
            if (x[0] == 'x' and y[0] == 'y') or (x[0] == 'y' and y[0] == 'x'):
                if op == 'XOR': res[int(x[1:])][0] = z
                else: res[int(x[1:])][1] = z
        
        carry = 'tss'
        for i in range(1, 44):
            print(f'x{i}', f'y{i}', carry)
            print(f'xor: {res[i][0]}, and: {res[i][1]}')
            rvp1, bcr1 = self.findLabel(carry, 'AND')
            rvp2, z012 = self.findLabel(carry, 'XOR')
            bcr2, carry = self.findLabel(res[i][1], 'OR')
            print(rvp1, rvp2)
            print(bcr1, bcr2)
            print('-------------')


    def findLabel(self, wire, op):
        for gate in self.gates:
            if gate[1] != op: continue
            if not(gate[0] == wire or gate[2] == wire): continue
            return (gate[0], gate[3]) if gate[2] == wire else (gate[2], gate[3])
    
    # solution found on paper using self.searchForVariables
    def solveP2(self): 
        return sorted(['cph', 'z19', 'gws', 'nnt', 'z13', 'npf', 'hgj', 'z33'])