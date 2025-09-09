def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    dict ={}
    used_char = set()
    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]
        print(s[i],'->',t[i])
        
        if c1 in dict:
            if dict[c1] != c2:
                return False
        else:
            
            

    
    print(dict,used_char)
    
    


s = "egg"
t = "add"
isIsomorphic(s, t)  # True → lengths are equal
