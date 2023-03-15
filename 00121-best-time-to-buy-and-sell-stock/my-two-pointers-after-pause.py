class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        n = len(prices)
        buy = 0
        
        while(buy < n):
            currProfit = 0
            sell = buy
            
            while(sell < n and prices[sell] >= prices[buy]):
                currProfit = max(currProfit, prices[sell] - prices[buy])
                
                sell += 1
            
            result = max(result, currProfit)
            
            buy = sell
            
        return result
