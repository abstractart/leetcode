class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        if len(prices) < 2:
            return 0
        
        buy = 0
        sell = 1
        
        while(buy <= sell and sell < len(prices)):            
            if prices[buy] >= prices[sell]:
                buy = sell
                sell = buy + 1
            else:
                result = max(result, prices[sell] - prices[buy])
                sell += 1
            
        
        return result
