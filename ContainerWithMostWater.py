def ContainerWithMostWater(arr):
    l = 0
    r = len(arr) - 1
    res = 0
    while l < r:
        dist = r - l
        min_no = min(arr[l] , arr[r])
        f_r = dist * min_no
        if f_r > res:
            res = f_r
        elif arr[l] < arr[r]:
            l+=1
        else:
            r-=1
    print(res)

   
print(ContainerWithMostWater([1,8,6,2,5,4,8,3,7])) #49