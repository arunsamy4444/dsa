def ImplementstrStr(str1,str2):
    if str2 == "":
        return 0
    for i in range(len(str1) - len(str2)):
        if str1[i:i+len(str2)] == str2:
            return i
    return -1
        
    
print(ImplementstrStr("hello", "ll"))
print(ImplementstrStr("abc", ""))      # 0
print(ImplementstrStr("aaaaa", "bba"))