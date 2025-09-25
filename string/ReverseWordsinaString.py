def ReverseWordsinaString(s):
    w = s.split(' ')
    new_str = []
    
    for i in w:
        if i != '':
            new_str.append(i)
            
    new_str.reverse()
    res=' '.join(new_str)          
    print(res)
   
    
print(ReverseWordsinaString("the sky is blue"))