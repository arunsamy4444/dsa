def IntersectionofTwoArraysII(arr1,arr2):
    d = {}
    res=[]
    for i in arr1:
        if i not in d:
            d[i] =1
        else:
            d[i]+=1
    for i in arr2:
        if i in d and d[i] > 0:
            res.append(i)
            d[i]-=1
    print(res)
    
print(IntersectionofTwoArraysII([1,2,2,1],[2,2]))
print(IntersectionofTwoArraysII([4,9,5],[9,4,9,8,4]))