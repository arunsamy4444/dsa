def ClimbingStairs(n):
    if n==1:
        print('1')
    if n==2:
        print('2')  
    dp = [1]*n
    dp[1] = 2
    
    for i in range(2,len(dp)):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    print(dp[-1]) 
    
print(ClimbingStairs(5)) #8