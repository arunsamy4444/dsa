def ReverseInteger(n):
    s= str(n)
    new_s = ''
    for i in s:
        if i=='-':
            continue
        new_s+=i
    rev_int = int(new_s[::-1])
    if n <0:
        rev_int = -rev_int
    print(rev_int)
    
print(ReverseInteger(-123))