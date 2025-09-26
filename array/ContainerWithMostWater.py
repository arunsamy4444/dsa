#------ SOL 1 ----- 
def ContainerWithMostWater(arr):
    l = 0
    r = len(arr)-1
    f_res = 0
    while l < r:
        dist = r-l #distance
        min_val = min(arr[l],arr[r])
        currnet_res = dist*min_val
        if currnet_res > f_res:
            f_res = currnet_res
        if arr[l] < arr[r]:
            l+=1
        else:
            r-=1
    print(f_res)
        

print(ContainerWithMostWater([1,8,6,2,5,4,8,3,7])) #49