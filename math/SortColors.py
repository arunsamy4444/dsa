
#------- Sol 2 --------
def SortColors(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    print(nums)

            

    
print(SortColors([10,1,45,21,88,100,2,3,5,1]))
# print(SortColors([1,0,2,0,1,2]))

#------- Sol 1 --------

# def SortColors(nums):
#     for i in range(0,len(nums)-1):
#         for j in range(0,len(nums)-1):
#             if nums[j] > nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]


#     print(nums)    
    
# print(SortColors([1,0,2,0,1,2]))