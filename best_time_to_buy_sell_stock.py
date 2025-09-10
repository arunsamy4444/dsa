def maxProfit(prices):
    n = len(prices)
    max_profit = 0
    
    for i in range(n):
        for j in range(i+1,n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
                print(f"Buy at ${prices[i]}, Sell at ${prices[j]}, Max Profit = {max_profit}")
    
    return max_profit
    

print(maxProfit([7,1,5,3,6,4]))  # Output: 5
# print(maxProfit([7,6,4,3,1]))    # Output: 0 (no profit possible)
# print(maxProfit([1,2,3,4,5]))    # Output: 4 (buy day 0, sell day 4)
# print(maxProfit([3,2,6,5,0,3]))  # Output: 4 (buy 2, sell 6)
