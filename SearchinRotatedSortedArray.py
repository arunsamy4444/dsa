def SearchinRotatedSortedArray(nums,tar):
    l,r=0,len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == tar:
            print(m)
        elif nums[m] < tar:
            l=m+1
        else:
            r=m-1
    return -1
    


print(SearchinRotatedSortedArray([4,5,6,7,0,1,2],0))
print(SearchinRotatedSortedArray([4,5,6,7,0,1,2],3))