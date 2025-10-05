def FindPeakElement(nums):
    for i in range(0,len(nums)-1):
        if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
            return i
    if len(nums) > 1 and nums[0] > nums[1]:
        return 0
    if len(nums) > 1 and nums[-1] > nums[-2]:
        return len(nums)-1
    if len(nums) == 1:
        return 0

    
    
print(FindPeakElement([1,0,1,3,5,6,4]))