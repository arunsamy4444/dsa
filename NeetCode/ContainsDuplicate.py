def ContainsDuplicate(nums):
    d = {}  
    for i in nums:
        if i in d:
            return True     
        d[i]=1
    return False
    
    
print(ContainsDuplicate([1, 2, 3, 3]))