from brainfuck import CompileBF
MyCompiler = CompileBF(StackAutoClear=False)
print('Enter your BF codes.\nFor get stack just type "stack"')
while True:
    try:
        code = input('---> : ')
        if code == 'stack':
            print(MyCompiler.Stack)
        elif code == 'clear':
            MyCompiler.ClearData()
            print('Done.')
        elif all(i in '[+-].,<>' for i in code):
            output = MyCompiler.ExectueCode(code)
            if output:
                print('output is :',output)
            print('pointer :', MyCompiler.Pointer)
        print('-'*15)
    except KeyboardInterrupt:
        break