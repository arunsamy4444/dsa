def maxprod(arr):
    maxNO=float('-inf')
    res=[]
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            prod = arr[i]*arr[j]
            if prod>maxNO:
                maxNO = prod
                res = [i,j]
    print('Indices',res)
    print("Max product:",maxNO)
    
maxprod([1, 10, 2, 6])