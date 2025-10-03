def TwoSumIIInputArrayIsSorted(nums,target):
    l,r=0,len(nums)-1
    while l < r:
        c = nums[l]+nums[r]
        if c == target:
            return [l+1,r+1]
        elif c < target:
            l+=1
        else:
            r-=1

    
print(TwoSumIIInputArrayIsSorted([2,7,11,15],9))