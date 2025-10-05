def IntersectionofTwoArrays(nums1,nums2):
    d = {}
    nums1=set(nums1)
    nums2=set(nums2)
    res = []
    for i in nums1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in nums2:
        if i in d:
            res.append(i)
    print(res)
    
    
print(IntersectionofTwoArrays([4,9,5],[9,4,9,8,4]))