def movezerotolast(arr):
    arr2=[]
    res=[]
    for i in arr:
        if i == 0:
            arr2.append(i)
        else:
            res.append(i)
            
    print(res+ arr2)
    return 

movezerotolast([0, 1, 0, 3, 12])