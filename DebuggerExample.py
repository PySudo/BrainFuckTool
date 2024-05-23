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
print(('-'*30)+' Method 2 '+('-'*30))
MyDebugger.ClearData()

# Also you can Debug a code like this without set code :
for i in MyDebugger.ReadAndDebug(MyCode):
    print(i)