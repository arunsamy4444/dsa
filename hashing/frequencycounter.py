def frequencyCounter(nums):
    d ={}
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print(d)

    
print(frequencyCounter([2,1,2,5,6,2,4,6,8,2,3,4,5,6,7,8,]))


# def frequencyCounter(nums):
#     dict = {}
#     for i in nums:
#         if i in dict:
#             dict[i]+=1
#         else:
#             dict[i]=i
#     print(dict)
            
    
    
# print(frequencyCounter([2,1,2,5,6,2,4,6,8,2,3,4,5,6,7,8,]))