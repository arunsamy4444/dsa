def rotate(nums, k):
    arr2=[]
    n = len(nums)
    
    k = k%n
    s = n-k
    
    res=[]
    for i in range(s,n): # loop og arr by taking range of k 
        arr2.append(nums[i]) # add to new arr
    for i in range(k,len(nums)-1):
        nums.pop() # remove elements in og arr by k 

    res = arr2 + nums # merge
    print(res)
    
    
rotate([1,2,3,4,5,6,7], 3)