
def maxProfit(prices):
    l=0
    r=1
    max=0
    while r < len(prices):
        diff = prices[r] - prices[l]
        if diff > max:
            max = diff
        if prices[r] < prices[l]: 
            l=r
        r+=1
    return max
    


print(maxProfit([7,6,4,3,1]))    # Output: 0 (no profit possible)
print(maxProfit([1,2,3,4,5]))    # Output: 4 (buy day 0, sell day 4)
print(maxProfit([3,2,6,5,0,3]))  # Output: 4 (buy 2, sell 6)