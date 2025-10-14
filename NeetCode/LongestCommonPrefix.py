def longestCommonPrefix(strs):
    strs.sort()
    # print(strs)
    f = strs[0]
    l = strs[-1]
    res = ''
    
    for i in range(min(len(f),len(l))):
        if f[i] == l[i]:
            res+=f[i]
        else: 
            break
    
    return res
        
    
    
    
print(longestCommonPrefix(["bat","bag","bank","band"]))