def ProductofArrayExceptSelf(nums):
    res= []
    for i in range(len(nums)):
        prod=1
        for j in range(len(nums)):
            if j!=i:
                prod*=nums[j]
        res.append(prod)
            
    print(res)
 
print(ProductofArrayExceptSelf([1,2,3,4])) #[24,12,8,6]




# def ProductofArrayExceptSelf(arr):
#     final = [1]*len(arr)
#     # print(final)
#     prefix = 1
#     for i in range(len(arr)):
#         # print(arr[i])
#         final[i] = prefix
#         prefix*=arr[i]
#         # print(final)
#     suffix = 1
#     for i in range(len(arr)-1,-1,-1):
#         final[i] *=suffix
        
#         suffix *=arr[i]
#     print(final)
        
# #just copied .... 
    
# print(ProductofArrayExceptSelf([1,2,3,4]))