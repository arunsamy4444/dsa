def GasStation(gas,cost):
    if sum(gas) < sum(cost):
        return -1
    p = 0
    st = 0
    for i in range(len(gas)):
        p+=gas[i]
        p-=cost[i]
        if p < 0:
            p=0
            st=i+1
    return st
    
    
    
print(GasStation([1,2,3,4,5] , [3,4,5,1,2]))