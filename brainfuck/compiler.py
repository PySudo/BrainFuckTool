class RangeError(Exception):
    pass

class CompileBF:
    def __init__(self, Code: str):
        self.code = Code
        self.stack = [0 for _ in range(100)]
        self.pointer = int()
        self.OUT = str()

    def __Shift(self, Right=True):
        if ( self.pointer >= 99 and Right ) or ( self.pointer <= 0 and not Right ):
            raise RangeError
        if Right:
            self.pointer += 1
        else:
            self.pointer -= 1
    
    @property
    def __Increase(self):
        self.stack[self.pointer] += 1
    
    @property
    def __Decrease(self):
        self.stack[self.pointer] -= 1
    
    def __Input(self, UserInput):
        self.stack[self.pointer] = sum(UserInput[0].encode())
    
    @property
    def __StdOut(self):
        self.OUT += chr(self.stack[self.pointer])

    def __ExectueJustLoop(self, Loop):
        while self.stack[self.pointer] != 1:
            self.__Execute(Loop)

    @property
    def __ResetOUT(self):
        self.stack = [0 for _ in range(100)]
        self.pointer = int()
        self.OUT = str()

    def __Execute(self, Code):
        for index, token in enumerate(Code):
            if token == '>':
                self.__Shift()
            elif token == '<':
                self.__Shift(False)
            elif token == '.':
                self.__StdOut
            elif token == ',':
                self.__Input(input())
            elif token == '+':
                self.__Increase
            elif token == '-':
                self.__Decrease
            elif token == '[':
                LoopIndex = Code[index+1::].find(']')
                LoopCode = Code[index+1:LoopIndex+index+1]
                self.__ExectueJustLoop(LoopCode)

    def __str__(self):
        self.__Execute(self.code)
        out = self.OUT
        self.__ResetOUT
        return out