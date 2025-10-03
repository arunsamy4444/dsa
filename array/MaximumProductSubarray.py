# def MaximumProductSubarray(nums):
#     max_prod = nums[0]
#     current = 1
#     for i in nums:
#         if current < 0:
#             current = 1
#         current*=i
#         if max_prod < current :
#             max_prod = current
#     return max_prod
    
    
# print(MaximumProductSubarray([2,3,-2,4])) #6