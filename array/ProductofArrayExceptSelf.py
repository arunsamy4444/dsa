def ProductofArrayExceptSelf(nums):
    res = [1]*len(nums)
    prefix=1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    suffix =1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= suffix
        suffix *=nums[i]
    print(res)
        

 
print(ProductofArrayExceptSelf([1,2,3,4])) #[24,12,8,6]


    # res= []
    # for i in range(len(nums)):
    #     prod=1
    #     for j in range(len(nums)):
    #         if j!=i:
    #             prod*=nums[j]
    #     res.append(prod)
            
    # print(res)