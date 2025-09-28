def SortColors(nums):
    while True:
        c=False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                c = True
        if not c:
            break
    print(nums)
                 
print(SortColors([1,0,2,0,1,2])) 
