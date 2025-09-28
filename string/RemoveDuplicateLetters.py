def RemoveDuplicateLetters(s):
    d = {}
    for i in s:
        if i in d:
            del d[i]
        d[i] = 1
    res = ''.join(d.keys())
    print(res)
    
print(RemoveDuplicateLetters("bcabc"))