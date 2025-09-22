def EvaluateReversePolishNotation(arr):
    stack = []
    l = ['+','-','*','/']
    for i in arr:
        if i not in l:
            stack.append(int(i))

        else:
            a=stack.pop()
            b=stack.pop()
            if i == '+':
                stack.append(a+b)
            elif i == '*':
                stack.append(b*a)
            elif i == '-':
                stack.append(b-a)
            elif i == '/':
                stack.append(int(b/a))
    print(stack)
    
print(EvaluateReversePolishNotation(['2','1','+','3','*'])) #9