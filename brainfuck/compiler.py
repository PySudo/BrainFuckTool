class RangeError(Exception):
    pass

class CompileBF:
    def __init__(self, Code: str = str(), StackAutoClear: bool = True):
        self.Code = Code
        self._auto = StackAutoClear
        self._stack = [0 for _ in range(100)]
        self.__pointer = int()
        self.OUT = str()

    @property
    def Code(self):
        return self._code

    @Code.setter
    def Code(self, code):
        if all(i in '.,[+-]<>\n' for i in code):
            self._code = code
        else:
            raise ValueError('it\'s not a brainfuck code!')

    def __Shift(self, Right=True):
        if ( self.__pointer >= len(self._stack)-1 and Right ) or ( self.__pointer <= 0 and not Right ):
            raise RangeError
        if Right:
            self.__pointer += 1
        else:
            self.__pointer -= 1

    @property
    def PointerValue(self):
        return self._stack[self.__pointer]
    
    @PointerValue.setter
    def PointerValue(self, NewValue):
        if isinstance(NewValue, int):
            self._stack[self.__pointer] = NewValue
        else:
            raise TypeError

    @property
    def Stack(self):
        return self._stack

    @Stack.setter
    def Stack(self, NewStack):
        if isinstance(NewStack, list):
            self._stack = NewStack
            self.__pointer = int()
        else:
            raise TypeError

    @property
    def Pointer(self):
        return self.__pointer
    
    @Pointer.setter
    def Pointer(self, NewValue):
        if 0 <= NewValue <= len(self._stack)-1:
            self.__pointer = NewValue
        else:
            raise RangeError

    def ClearData(self):
        self._stack = [0 for _ in range(100)]
        self.__pointer = int()
        self.OUT = str()
        self.Code = str()

    def __Input(self, UserInput):
        self._stack[self.__pointer] = sum(UserInput[0].encode())
    
    def _StdOut(self):
        if self._stack[self.__pointer] >= 0:
            self.OUT += chr(self._stack[self.__pointer])

    def PrintStackAsChar(self):
        return ''.join(chr(i) for i in self._stack if i)

    def _ExectueLoop(self, Loop):
        while self._stack[self.__pointer] != 1:
            self.ExectueCode(Loop, True)

    def ExectueCode(self, Code=str(), Loop=False, inputText=str()):
        if not Code:
            Code = self.Code
        for index, token in enumerate(Code):
            if token == '>':
                self.__Shift()
            elif token == '<':
                self.__Shift(False)
            elif token == '.':
                self._StdOut()
            elif token == ',':
                if inputText:
                    print(inputText, end='')
                self.__Input(input())
            elif token == '+':
                self.PointerValue += 1
            elif token == '-':
                self.PointerValue -= 1
            elif token == '[':
                LoopIndex = Code[index+1::].find(']')
                LoopCode = Code[index+1:LoopIndex+index+1]
                self._ExectueLoop(LoopCode)
        if not Loop:
            out = self.OUT
            if self._auto:
                self.ClearData()
            return out

    def __str__(self):
        out = self.ExectueCode(self.Code)
        if self._auto:
            self.ClearData()
        return out