def ImplementstrStr(str1,str2):
    if str2 == "":
        return 0
    for i in range(len(str1) - len(str2)):
        if str1[i:i+len(str2)] == str2:
            return i
    return -1
        
        
    # for i,v in enumerate(str1):
    #     # print(f'{i} --> {v}')
    #     if v == str2[0]:
    #         if str2 == str1[i:i+len(str2)]:
    #             return (i)
    # return -1
  
    
print(ImplementstrStr("hello", "ll"))
print(ImplementstrStr("abc", ""))      # 0
print(ImplementstrStr("aaaaa", "bba"))