class String2BF:
    def __init__(self, text: str):
        self.text = text

    def __GetValue(self, ASCII):
        for i in range(10,1,-1):
            if not ASCII%i:
                return i
        return ASCII

    def __CreateForLoop(self, Times, ASCII, Shift = 1, Extra = {'inc': 0, 'dec': 0}):
        ForStorage = ASCII//Times
        EX = '+' if Extra['dec'] else '-' if Extra['inc'] else ''
        return f"{EX}{'>'*Shift}{'+'*Times}[{'<'*Shift}{'+'*ForStorage}{'>'*Shift}-]{'<'*Shift}"

    def __DetectINCorDEC(self, Number):
        Num = Number+1
        Num2 = Number-1
        NumMin = float('inf')
        NumMX = int()
        for i in range(10,1,-1):
            if not Num%i and i > NumMX:
                NumMX = i
            if not Num2%i and i < NumMin:
                NumMin = i
        return {'dec': NumMin, 'inc': 0, 'type': 0} if NumMin > NumMX else {'dec': 0, 'inc': NumMX, 'type': 1}

    def __Prime(self, Number):
        Detect = self.__DetectINCorDEC(Number)
        if Detect['type']:
            Number += 1
            times = Detect['inc']
        else:
            Number -= 1
            times = Detect['dec']
        return self.__CreateForLoop(times, Number, Extra=Detect)

    def __Convert(self, ASCII):
        Value = self.__GetValue(ASCII)
        if Value == ASCII:
            return self.__Prime(ASCII)
        return self.__CreateForLoop(Value, ASCII)

    def __S2BF(self, String):
        OUT = list()
        for i in String.encode():
            OUT.append(self.__Convert(i))
        return '.>'.join(OUT)+'.'

    def __str__(self):
        return self.__S2BF(self.text)
