def ValidAnagram(s,t):
    
    
    if len(s) != len(t):
        return False
    
    res = {}
    
    for i in s:
        if i in res:
            res[i]+=1
        else:
            res[i]=1
    for i in t:
        if i not in res or res[i] == 0:
            return False
        else:
            res[i]-=1
    
    return True

    
    
    
print(ValidAnagram("racecar","carrace"))