from .compiler import CompileBF

class Debug(CompileBF):
    def __GetStackIndex(self, Stack):
        for index, value in enumerate(Stack[::-1]):
            if value:
                return Stack[0:1+len(Stack)-(index+1)]

    def __ExtractTokens(self, Code):
        currentToken = str()
        Tokens = list()
        for index, value in enumerate(Code):
            if value != currentToken:
                Tokens.append({'token': value, 'start': index, 'stop': index})
                currentToken = value
            elif currentToken:
                Tokens[-1]['stop'] = index
        return Tokens

    def GetInformation(self, info, LoopCode):
        token = info['token']
        if token == '+':
            action = 'increase'
            desc = 'This is incrementing the value from {} to {} at stack index {}'.format(self.PointerValue, self.PointerValue+(info['stop']-info['start']+1), self.Pointer)
        elif token == '-':
            action = 'decrease'
            desc = 'This is decreasing the value from {} to {} at stack index {}'.format(self.PointerValue, self.PointerValue-(info['stop']-info['start']+1), self.Pointer)
        elif token == '>':
            action = 'right shift'
            desc = 'This is shifting to right from index {} to {} in stack'.format(self.Pointer, self.Pointer+(info['stop']-info['start']+1))
        elif token == '<':
            action = 'left shift'
            desc = 'This is shifting to left from index {} to {} in stack'.format(self.Pointer, self.Pointer-(info['stop']-info['start']+1))
        elif token == '.':
            action = 'standard output'
            desc = 'This prints stack index {} with value {} as ascii'.format(self.Pointer, self.PointerValue)
        elif token == ',':
            action = 'standard input'
            desc = 'This is will get a input and save that in {} stack index'.format(self.Pointer)
        elif token == '[':
            action = 'Start a loop'
            desc = 'This start a loop and continue to execute anything betweeb of [] for {} times'.format(self.PointerValue)
            print(str('{}Token [LOOP] is : {}\nNumber of tokens : {}\nAction : {}\nDescription : {}'.format(('-'*10)+'\n', token, info['stop']-info['start']+1, action, desc)))
        elif token == ']':
            action = 'Stop loop'
            desc = 'This is end of the last loop\nLoop Code : {}'.format(LoopCode)
        return action, desc

    def ReadAndDebug(self, Code):
        if Code is None:
            Code = self._code
        tokens = self.__ExtractTokens(Code)
        print('Number of Tokens :',str(len(tokens)))
        Loop = False
        LoopCode = str()
        stackStatus = '\nStack status after execute : {}'
        times = int()
        for index, info in enumerate(tokens):
            token = info['token']
            action, desc = self.GetInformation(info, LoopCode)
            if token in '[':
                times = self.PointerValue
                Loop = True
            if token == ']' and Loop:
                Loop = False
                for _ in range(times):
                    self.ExectueCode(LoopCode)
                LoopCode = str()
            if Loop:
                if token not in '[]':
                    LoopCode += token*(info['stop']-info['start']+1)
                continue
            self.ExectueCode(token*(info['stop']-info['start']+1), inputText='{}\nEnter a value for save in index {} : '.format('-'*10, index+1, self.Pointer))
            stackRange = self.__GetStackIndex(self._stack)
            if stackRange:
                status = stackStatus.format(stackRange)
            else:
                status = str()
            yield str('{}Token {} is : {}\nNumber of tokens : {}\nAction : {}\nDescription : {}{}'.format(('-'*10)+'\n' if token != ',' else '', index+1, token, info['stop']-info['start']+1, action, desc, status))
    def __iter__(self):
        return self.ReadAndDebug(self._code)