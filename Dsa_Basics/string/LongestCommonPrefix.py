def longestCommonPrefix(strs):
    if not strs:
        return ''
    
    strs.sort()

    f = strs[0]
    l = strs[-1]
    res = ''
    for i in range(min(len(f),len(l))):
        if l[i] == f[i]:
            res+=l[i]
        else:
            break
    return res
    
print(longestCommonPrefix(["flower","flow","flight"]))  
print(longestCommonPrefix(["dog","racecar","car"]))   
print(longestCommonPrefix(["interspecies","interstellar","interstate"]))  