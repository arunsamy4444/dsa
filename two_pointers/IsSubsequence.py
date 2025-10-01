def IsSubsequence(s,t):
    p1=0
    p2=0
    while p1 < len(s) and p2 < len(t):
        if t[p2] == s[p1]:
            p1+=1
            p2+=1
        else:
            p2+=1
    if p1 == len(s):
        return True
    else:
        return False
            
    
print(IsSubsequence("abc","ahbgdc"))