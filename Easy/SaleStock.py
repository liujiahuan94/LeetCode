def maxProfit(sprices: List[int]) -> int:
    if len(prices) < 2:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    for i in prices:
        min_price = min(i, min_price)
        max_profit = max(max_profit, i - min_price)
    
    return max_profit