def FindtheDifference(s,t):
    d = {}
    str = s + t
    for i in str:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in d:
        if d[i] ==1:
            print(i)
  
print(FindtheDifference("abcd","abcde"))