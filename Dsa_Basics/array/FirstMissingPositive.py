def FirstMissingPositive(nums):
    nums.sort()
    print(nums)
    for i in range(0,len(nums)):
        if nums[i] != i:
            print(i)
    print(len(nums))
    
print(FirstMissingPositive([1,2,0]))