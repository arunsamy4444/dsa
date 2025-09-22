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




# #------ SOL 1 ----- 
# def ContainerWithMostWater(arr):
#     l = 0
#     r = len(arr)-1
#     f_res = 0
#     while l < r:
#         d = r-l  #index val
#         min_val = min(arr[l],arr[r])
#         c_res = d*min_val
#         f_res = max(c_res,f_res)
    
#         if arr[l] < arr[r]:
#             l+=1
#         else:
#             r-=1
#     print(f_res)
   
# print(ContainerWithMostWater([1,8,6,2,5,4,8,3,7])) #49

#------ SOL 2 ----- 


# def ContainerWithMostWater(arr):
#     l = 0
#     r = len(arr) - 1
#     res = 0
#     while l < r:
#         dist = r - l
#         min_no = min(arr[l] , arr[r])
#         f_r = dist * min_no
#         if f_r > res:
#             res = f_r
#         elif arr[l] < arr[r]:
#             l+=1
#         else:
#             r-=1
#     print(res)

   
# print(ContainerWithMostWater([1,8,6,2,5,4,8,3,7])) #49