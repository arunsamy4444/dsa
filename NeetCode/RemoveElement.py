def RemoveElement(nums,val):
    c = 0
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            c+=1
            i-=1
        i+=1
    return nums

    
print(RemoveElement([1,1,2,3,4],1))