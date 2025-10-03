def CheckIfNandItsDoubleExist(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in nums:        
        if i==0:
            if d[i] >1:
                return True
        else:
            if 2*i in d:
                return True
    return False

    
print(CheckIfNandItsDoubleExist([10,2,5,3])) #true