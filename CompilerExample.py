from brainfuck import CompileBF
MyCompiler = CompileBF(StackAutoClear=False)
# i set StackAutoClear to "False" cuz this is will not destroy stack after execute brainfck codes and hold the data
# now you can have access to Stack and Pointer and etc just like this :
print(MyCompiler.Stack)          # This will show stack
print(MyCompiler.Pointer)        # This show pointer location (pointer index in stack list) 
print(MyCompiler.PointerValue)   # This show you the "MyCompiler.Pointer" points to what value in stack
print('-*'*60)
# Also you can change pointer and stack and etc lile this :
MyCompiler.Stack = [10, 20, 29, 40]  # This will set [10, 20, 29, 40] list as stack
MyCompiler.Pointer = 2               # This will set pointer to index 3 in stak list
MyCompiler.PointerValue = 20         # This will set 20 as MyCompiler.Stack[MyCompiler.Pointer]
# You can Execute BrainFuck codes and get output like this :
MyCompiler.ClearData() # This make stack and pointer empty
output = MyCompiler.ExectueCode('->+++++++[<++++++++++++++>-]+++++[>+++++<-]>[<<.+>>-]<<.')
print(MyCompiler.Stack)
print('pointer :',MyCompiler.Pointer)
print('pointer value :',MyCompiler.PointerValue)
print('output is :',output)
print('-*'*60)
# You can get output from stack datas without using "." in BF code :
MyCompiler.Stack = [ord(i) for i in 't.me/Py_Sudo']
print(MyCompiler.PrintStackAsChar())
MyCompiler.ClearData()
print('-*'*60)
# You can set code like this :
MyCompiler.Code = '>++++[<+++++++++++++++++++++++++++++>-]<.>>++[<+++++++++++++++++++++++>-]<.>->++++++++++[<+++++++++++>-]<.>->++++++[<+++++++++++++++++>-]<.>->++++++++[<++++++>-]<.>>++++++++++[<++++++++>-]<.>->++[<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]<.>>+++++[<+++++++++++++++++++>-]<.>->+++++++[<++++++++++++>-]<.>>+++++++++[<+++++++++++++>-]<.>>++++++++++[<++++++++++>-]<.>>+++[<+++++++++++++++++++++++++++++++++++++>-]<.'
# Then you can execute that like this :
print('result is :', MyCompiler.ExectueCode())