# 21.05.2022 - not accepted
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        s = []
        s.append((0, amount, 0))  
        
        result = float("inf")
        while(len(s) > 0):
            count, curr_amount, curr_index = s.pop()
            if curr_amount == 0:
                result = min(result, count)
                continue
            
            
            for i in reversed(range(curr_index, len(coins))):
                if curr_amount - coins[i] >= 0:
                    counts = curr_amount // coins[i]
                    if count + counts < result:
                        s.append((count + 1, curr_amount - coins[i], i))
                    
        
        return (-1 if result == float("inf") else result)
