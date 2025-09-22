def ReverseString(str):
    l = 0
    r = len(str) - 1
    while l <= r:
        str[l],str[r] = str[r],str[l]
        l+=1
        r-=1
    print(str)
    
    
print(ReverseString(['A','R','U','N','S','A','M','Y']))