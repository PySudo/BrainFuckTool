# BrainFuckTool

This is the most complete "brainfuck" language tool

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install brainfuck tool.

```bash
pip install brainfuck-tool
```
if you install this package using pip , just use `brainfucktool.shell()` function for using shell

## Usage

- String to brainfuck code :
```python
from brainfucktool import String2BF

print(String2BF('Hello World :)'))
# output is a brainfuck code that output is "Hello World :)"
```
this is working with `__str__` so use `str()` for variables , like this :
```python
variable = str(String2BF('Hello World :)'))
```

- Compiler :
```python
from brainfucktool import CompileBF

print(CompileBF('''
>+++++++[<+++++++++++++++>-]<.
>>++++++++[<++++>-]<.
>->+++++++[<++++++++++++++>-]<.
>->++++++++++[<+++++++++++>-]<.
>>++++++++[<++++>-]<.
>>+++++++++[<++++++++++++>-]<.
>>+++[<+++++++++++++++++++++++++++++++++++++>-]<.
>>+++++++++[<+++++++++++>-]<.
>->+++++++[<++++++++++++++>-]<.
>>+++++++++[<++++++++++++>-]<.
>>++++++++[<+++++++++++++>-]<.
>>+++[<+++++++++++++++++++++++++++++++++++++>-]<.
>>+++++[<+++++++++++++++++++++++>-]<.
>>++++[<+++++++++++++++++++++++++++++>-]<.'''))
# output is : i am localhost
# Also you can write that in one line...
```

- Debugger :
```python
from brainfucktool import Debug

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
```