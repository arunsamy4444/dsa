def two_sum(nums, tar):
    l = 0
    r = len(nums)-1
    while l < r:
        res = nums[l] + nums[r]
        if res == tar:
            return [l+1,r+1]
        elif res > tar:
            r-=1
        else:
            l+=1
    return []
    

print(two_sum([1, 2, 3, 4] , 3)) #[1, 2]