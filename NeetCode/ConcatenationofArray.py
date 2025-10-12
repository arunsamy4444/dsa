def ConcatenationofArray(nums):
    res = []
    for i in nums:
        res.append(i)
    for i in nums:
        res.append(i)
    return res

    
print(ConcatenationofArray([1,4,1,2]))   #[1,4,1,2,1,4,1,2]



    # res = nums + nums
    # return res
    