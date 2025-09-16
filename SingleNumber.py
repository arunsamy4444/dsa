def SingleNumberOne_and_three(nums):
    d = {}
    for i in nums:
        if i in d:
            del d[i]
        else:
            d[i]=1
    a = list(d.keys())
    print(a)
    
print(SingleNumberOne_and_three([1,2,4,2,1,5]))