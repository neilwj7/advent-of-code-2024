from copy import deepcopy
class solution:
    def __init__(self, inputFile):
        self.registers, self.program = self.getInput(inputFile)

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
    
    def solveP1(self):
        return self.runProgram()
    
    def solveP2(self):
        target = self.program[::-1]
        return self.helper(target, 0, 0)

    def helper(self, target, i, ps):
        if i == len(target):
            return ps
        
        ps = ps << 3
        for n in range(8):
            if self.myProgram(ps + n) == target[i]:
                res = self.helper(target, i + 1, ps + n)
                if res != -1:
                    return res
        return -1

    def myProgram(self, a):
        b = a % 8
        b = b ^ 3
        c = a >> b
        b = b ^ c
        a = a >> 3
        b = b ^ 5
        return b % 8
            
    def runProgram(self):
        a, b, c = 4, 5, 6

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