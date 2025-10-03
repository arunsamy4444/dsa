def sortedSquares(nums):
    sq = []
    for i in nums:
        sq.append(i*i)
    sq.sort()
    print(sq)
    
    
    
print(sortedSquares([-4,-1,0,3,10])) #[0,1,9,16,100]