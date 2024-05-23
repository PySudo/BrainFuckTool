from brainfuck import Debug
MyCode = '->+++++++[<++++++++++++++>-]+++++[>+++++<-]>[<<.+>>-]<<.'
MyDebugger = Debug(StackAutoClear=False)
MyDebugger.Code = MyCode
print(('-'*5)+' Start Debugging '+('-'*5))
for i in MyDebugger:
    print(i)