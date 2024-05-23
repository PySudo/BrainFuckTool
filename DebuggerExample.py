from brainfuck import Debug

# Your BrainFuck Code :
MyCode = '>++[<+++>-]'

# Create a instance :
MyDebugger = Debug(StackAutoClear=False) # Also you can get code like "Debug(Mycode, StackAutoClear=False)"

# Set Brainfuck Code :
MyDebugger.Code = MyCode

# Start Debugging :
print(('-'*5)+' Start Debugging '+('-'*5))
for i in MyDebugger:
    print(i)