def ThreeSum(arr):
    if len(arr) < 3:
        return []
    arr.sort()
    res = []
    # print(arr)
    for i in range(len(arr)-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        
        # print(i)
        l = i+1
        r = len(arr)-1
        while l < r:
            s = arr[i] + arr[l] + arr[r]        
            # print(s)
            if s == 0:
                res.append([arr[i],arr[l],arr[r]])
                l+=1
                r-=1
                while l < r and arr[l] == arr[l-1]:
                    l+=1
                while l < r and arr[r] == arr[r+1]:
                    r-=1
                
            elif s < 0:
                l+=1
            elif s >0:
                r-=1
    print(res)
        
print(ThreeSum([-1,0,1,2,-1,-4]))