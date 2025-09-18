def ValidParentheses(s):
    stack = []
    d = {'[':']','{':'}','(':')'}
    for i in s:
        if i in d.keys():
            stack.append(i)
        else:
            if stack == []:
                print("False ))))))")
            else:
                if d[stack[-1]] == i:
                    stack.pop()
                else:
                    print('False ......')
    
    
    if stack == []:
        print('True')   
    else:
        print('False')  
    
    
    
    
    
    
    
    
    
    
    
    
    
    # stack = []
    # d = {'[':']','{':'}','(':')'}
    # for i in s:
    #     if i in d.keys():
    #         stack.append(i)
    #     else:
    #         if stack == []:
    #             print('False')   
    #         else:
    #             if d[stack[-1]] == i:
    #                 stack.pop()
    #             else:
    #                 print('False')   
    # if stack == []:
    #     print('True')   
    # else:
    #     print('False')                
            
        
    
    
print(ValidParentheses('(){}[]'))
print(ValidParentheses('){}[]'))