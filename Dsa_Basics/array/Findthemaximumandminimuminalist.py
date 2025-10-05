def Findthemaximumandminimuminalist(arr):
    arr.sort()

    max = arr[-1]
    min = arr[0]
    print('MAX ->',max)
    print('MIN ->',min)
    
print(Findthemaximumandminimuminalist([3, 7, 1, 9]))