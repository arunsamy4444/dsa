def FindAllNumbersDisappearedinanArray(nums):
    a = sorted(set(nums))
    res = []
    for x in range(1,a[0]):
        res.append(x)
        
    for i in range(len(a)-1):
        diff = a[i+1] - a[i]
        if diff > 1:
            for x in range(1,diff):               
                res.append(a[i]+x)
                
    for x in range(a[-1]+1, len(nums)+1):
        res.append(x)
        
    return res

               
    
print(FindAllNumbersDisappearedinanArray([4,3,2,7,8,2,3,1]))  # [5,6]