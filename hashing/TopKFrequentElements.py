def TopKFrequentElements(nums,k):
    d = {}

    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    sorted_items = sorted(d.items() , key=lambda x: x[1],reverse=True)
    res= []
    for i in range(k):
        res.append(sorted_items[i][0])
    print(res)  
    
print(TopKFrequentElements([1,1,1,2,2,3], 2)) #[1,2]