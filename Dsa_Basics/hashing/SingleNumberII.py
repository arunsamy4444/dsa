def SingleNumberII(nums):
    
    count ={}
    for i in nums:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for k,v in count.items():
        if v==1:
            print(k)
    
    
print(SingleNumberII([0,1,0,1,0,1,99]))
