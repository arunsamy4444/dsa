def BaseBall(arr):
    stack = []
    for i in arr:
        if i == 'C':
            stack.pop()
        elif i == 'D':
            stack.append(stack[-1]*2)
        elif i == '+':
            stack.append(stack[-1]+stack[-2])
        else:
            stack.append(int(i))
    print(sum(stack))
        
    
print(BaseBall(["5","-2","4","C","D","9","+","+"]))
# If integer → push.

# If "C" → pop.

# If "D" → push 2 * last.

# If "+" → push sum(last two).