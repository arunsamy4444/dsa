def HowManyNumbersAreSmallerThantheCurrentNumber(nums):
    # sorted_nums = sorted(nums)
    res = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i]>nums[j]:
                count+=1
        res.append(count)
    return res
    

        
    

    
    
print(HowManyNumbersAreSmallerThantheCurrentNumber([8,1,2,2,3])) #[4,0,1,1,3]