def ReplaceElementswithGreatestElementonRightSide(arr): 
    res = []
    max_val = -1
    for i in range(len(arr)-1,-1,-1):
        res.append(max_val)
        # print(arr[i])
        if max_val < arr[i]:
            max_val = arr[i]
    print(res[::-1])
    
print(ReplaceElementswithGreatestElementonRightSide([17,18,5,4,6,1]))   #[18,6,6,6,1,-1]



    # res=[]
    # for i in range(len(nums)):
    #     max_val = float('-inf')
    #     for j in range(i+1,len(nums)):
    #         if nums[j] > max_val:
    #             max_val = nums[j]
    
    #     res.append(max_val)
    # res[-1]=-1
    # print(res)