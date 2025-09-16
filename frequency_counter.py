def frequencyCounter(nums):
    dict = {}
    for i in nums:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=i
    print(dict)
            
    
    
print(frequencyCounter([2,1,2,5,6,2,4,6,8,2,3,4,5,6,7,8,]))