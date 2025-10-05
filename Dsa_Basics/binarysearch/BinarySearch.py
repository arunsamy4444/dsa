def BinarySearch(nums , tar):
    l=0
    r=len(nums)-1

    while l <= r:
        m = (l+r)//2
        if nums[m] == tar:
            return m
        elif nums[m] < tar:
            l = m+1
        elif nums[m] > tar:
            r = m-1
    return -1
    
    
print(BinarySearch([-1,0,3,5,9,12] , 98)) 
print(BinarySearch([-1,0,3,5,9,12] , 9))