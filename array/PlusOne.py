def PlusOne(arr):
    num = int(''.join(map(str,arr)))
    # print(num)    
    res = num + 1
    # print(res)
    final_res = []
    for i in str(res):
        
        final_res.append(int(i))
    print(final_res)
        
        
    
    
print(PlusOne([1,2,3]))   # [1,2,4]
print(PlusOne([4,3,2,1])) # [4,3,2,2]
print(PlusOne([9,9,9]))   # [1,0,0,0]
