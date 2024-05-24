# BrainFuckTool

This is the most complete "brainfuck" language tool

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install brainfuck tool.

```bash
pip install brainfuck-tool
```

## Usage
- if you install this package using pip , just use `brainfucktool.shell()` function for using shell

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
# Compiler :
- simple execution :
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
## Compiler customization
- get the stack and pointer values :
 ```python
from brainfuck import CompileBF
MyCompiler = CompileBF(StackAutoClear=False)
# i set StackAutoClear to "False" cuz this is will not destroy stack after execute brainfck codes and hold the data
# now you can have access to Stack and Pointer and etc just like this :
print(MyCompiler.Stack)          # This will show stack
print(MyCompiler.Pointer)        # This show pointer location (pointer index in stack list) 
print(MyCompiler.PointerValue)   # This show you the "MyCompiler.Pointer" points to what value in stack
```
- set value for pointer and stack and brainfuck code to instance :
```python
# You can change pointer and stack and etc like this :
MyCompiler.Stack = [10, 20, 29, 40]  # This will set [10, 20, 29, 40] list as stack
MyCompiler.Pointer = 2               # This will set pointer to index 3 in stak list
MyCompiler.PointerValue = 20         # This will set 20 as MyCompiler.Stack[MyCompiler.Pointer]
# You can set a code and execute that like this :
MyCompiler.Code = '>++++[<+++++++++++++++++++++++++++++>-]<.>>++[<+++++++++++++++++++++++>-]<.>->++++++++++[<+++++++++++>-]<.>->++++++[<+++++++++++++++++>-]<.>->++++++++[<++++++>-]<.>>++++++++++[<++++++++>-]<.>->++[<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]<.>>+++++[<+++++++++++++++++++>-]<.>->+++++++[<++++++++++++>-]<.>>+++++++++[<+++++++++++++>-]<.>>++++++++++[<++++++++++>-]<.>>+++[<+++++++++++++++++++++++++++++++++++++>-]<.'
# Then you can execute that like this :
print('result is :', MyCompiler.ExectueCode())
```
- execute a brainfuck code with compiler instance :
```python
# Also you can Execute BrainFuck codes and get output like this :
output = MyCompiler.ExectueCode('->+++++++[<++++++++++++++>-]+++++[>+++++<-]>[<<.+>>-]<<.')
print(MyCompiler.Stack)
print('pointer :',MyCompiler.Pointer)
print('pointer value :',MyCompiler.PointerValue)
print('output is :',output)
```
- get ASCII output from stack :
```python
# You can get output from stack datas without using "." in BF code :
MyCompiler.Stack = [ord(i) for i in 't.me/Py_Sudo']
print(MyCompiler.PrintStackAsChar())
```
- clear instance datas :
```python
MyCompiler.ClearData() # This make stack and pointer and etc empty
```
# Debugger :
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
