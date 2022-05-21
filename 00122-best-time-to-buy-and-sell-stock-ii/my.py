class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        i = 0
        n = len(prices)
        
        while(i < n):
            index, profit = self.firstGoodDeal(prices, i, n)
            if index == i: break
            
            result += profit
            i = index
        
        return result
        
        
    def firstGoodDeal(self, prices, start, finish):
        minPrice = float("inf")
        profit = 0
        index = start
        
        for i in range(start, finish):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > 0:
                return [i, prices[i] - minPrice]
        
        return [index, profit]
