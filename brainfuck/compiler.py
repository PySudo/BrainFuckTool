class RangeError(Exception):
    pass

class CompileBF:
    def __init__(self, Code: str = str(), StackAutoClear: bool = True):
        self.code = Code
        self._auto = StackAutoClear
        self.__stack = [0 for _ in range(100)]
        self.__pointer = int()
        self.OUT = str()

    def __Shift(self, Right=True):
        if ( self.__pointer >= len(self.__stack)-1 and Right ) or ( self.__pointer <= 0 and not Right ):
            raise RangeError
        if Right:
            self.__pointer += 1
        else:
            self.__pointer -= 1
    
    @property
    def PointerValue(self):
        return self.__stack[self.__pointer]
    
    @PointerValue.setter
    def PointerValue(self, NewValue):
        if isinstance(NewValue, int):
            self.__stack[self.__pointer] = NewValue
        else:
            raise TypeError

    @property
    def Stack(self):
        return self.__stack

    @Stack.setter
    def Stack(self, NewStack):
        if isinstance(NewStack, list):
            self.__stack = NewStack
            self.__pointer = int()
        else:
            raise TypeError

    @property
    def Pointer(self):
        return self.__pointer
    
    @Pointer.setter
    def Pointer(self, NewValue):
        if 0 <= NewValue <= len(self.__stack)-1:
            self.__pointer = NewValue
        else:
            raise RangeError

    def ClearData(self):
        self.__stack = [0 for _ in range(100)]
        self.__pointer = int()
        self.OUT = str()

    def __Input(self, UserInput):
        self.__stack[self.__pointer] = sum(UserInput[0].encode())
    
    def _StdOut(self):
        if self.__stack[self.__pointer] >= 0:
            self.OUT += chr(self.__stack[self.__pointer])

    def PrintStackAsChar(self):
        return ''.join(chr(i) for i in self.__stack if i)

    def __ExectueLoop(self, Loop):
        while self.__stack[self.__pointer] != 1:
            self.ExectueCode(Loop, True)

    def ExectueCode(self, Code, Loop=False):
        for index, token in enumerate(Code):
            if token == '>':
                self.__Shift()
            elif token == '<':
                self.__Shift(False)
            elif token == '.':
                self._StdOut()
            elif token == ',':
                self.__Input(input())
            elif token == '+':
                self.PointerValue += 1
            elif token == '-':
                self.PointerValue -= 1
            elif token == '[':
                LoopIndex = Code[index+1::].find(']')
                LoopCode = Code[index+1:LoopIndex+index+1]
                self.__ExectueLoop(LoopCode)
        if not Loop:
            out = self.OUT
            if self._auto:
                self.ClearData()
            return out

    def __str__(self):
        out = self.ExectueCode(self.code)
        if self._auto:
            self.ClearData()
        return out