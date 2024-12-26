class solution:
    def __init__(self, inputFile):
        self.registers, self.program = self.getInput(inputFile)
        self.p = self.getStringProgram()

    def getInput(self, fileName):
        program, registers = [], [i for i in range(7)]
        with open(fileName, 'r') as file:
            i = 0
            for line in file:
                if i < 3:
                    registers[i + 4] = int(line.strip()[12:])
                elif i > 3:
                    for num in line[9:].strip().split(','):
                        program.append(int(num))
                i += 1
        return registers, program
    
    def getStringProgram(self):
        res = str(self.program[0])
        for i in range(1, len(self.program)):
            res += str(',' + str(self.program[i]))
        return res
    
    def solveP1(self):
        return self.runProgram()
    
    def solveP2(self):
        # binary search on the answer
        l, r = 0, 1000000000000000
        b = 0
        while l < r:
            m = l + (r - l) // 2
            self.registers[4] = m
            s = self.runProgram()
            if s == 'INFINITE':
                l += 2
                continue
            elif s == self.p:
                return m
            elif len(s) < len(self.p):
                l = m + 1
            elif len(s) > len(self.p):
                r = m - 1
            else:
                b = m
                break
        if b == 0:
            return 0
        
        print("here")
        save = b
        while True:
            self.registers[4] = b
            s = self.runProgram()
            if s == self.p:
                return b
            if s == 'INFINITE':
                b += 1
                continue
            elif len(s) > len(self.p):
                break
            b += 1
        print("here")
        b = save
        res = b
        while True:
            self.registers[4] = b
            s = self.runProgram()
            if s == self.p:
                res = b
            if len(s) < len(self.p):
                return res
            b -= 1
            

        return 0
            
    def runProgram(self):
        a, b, c = 4, 5, 6
        preventLoop = set()

        res = ""
        i = 0
        while i < len(self.program):
            if self.program[i] == 0:
                # adv
                self.registers[a] = self.registers[a] // (2 ** self.registers[self.program[i + 1]])
                i += 2
            elif self.program[i] == 1:
                # bxl
                self.registers[b] = self.registers[b] ^ self.program[i + 1]
                i += 2
            elif self.program[i] == 2:
                # bst
                self.registers[b] = self.registers[self.program[i + 1]] % 8
                i += 2
            elif self.program[i] == 3:
                # jnz
                if (i, self.program[i + 1], self.registers[a], self.registers[b], self.registers[c]) in preventLoop:
                    return 'INFINITE'
                preventLoop.add((i, self.program[i + 1], self.registers[a], self.registers[b], self.registers[c]))
                if self.registers[a] == 0:
                    i += 2
                else:
                    i = self.program[i + 1]
            elif self.program[i] == 4:
                # bxc
                self.registers[b] = self.registers[b] ^ self.registers[c]
                i += 2
            elif self.program[i] == 5:
                # out
                v = str(self.registers[self.program[i + 1]] % 8)
                if res == '':
                    res = v
                else:
                    res = res + ',' + v
                i += 2
            elif self.program[i] == 6:
                # bdv
                self.registers[b] = self.registers[a] // (2 ** self.registers[self.program[i + 1]])
                i += 2
            elif self.program[i] == 7:
                # cdv
                self.registers[c] = self.registers[a] // (2 ** self.registers[self.program[i + 1]])
                i += 2
        return res