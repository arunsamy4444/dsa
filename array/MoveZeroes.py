
def MoveZeroes(nums):
    l=0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[l],nums[i] = nums[i],nums[l]
            l+=1
    print(nums)

      
    
print(MoveZeroes([0,1,0,3,12])) #[1,3,12,0,0]






















    # l=0
    # for i in range(len(nums)):
    #     if nums[i] !=0:
    #         nums[l],nums[i] = nums[i],nums[l]
    #         l+=1
    # print(nums)