def MajorityElementII(nums):
    x = len(nums)//3    
    res = {}  
    for i in nums:
        if i in res:
            res[i]+=1
        else:
            res[i]=1         
    op = []      
    for k,v in res.items():
        if v > x:
            op.append(k)
    return op
            
        
print(MajorityElementII([5,2,3,2,2,2,2,5,5,5])) #[2,5]