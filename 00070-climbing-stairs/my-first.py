import math

class Solution:
    def climbStairs(self, n: int) -> int:
        result = 0
        
        steps_2 = 0
        while(steps_2 * 2 <= n):
            result += self.variants_count(steps_2, n - steps_2 * 2)
            steps_2 += 1
            
        return result
            
    
    def variants_count(self, steps_1, steps_2):
        return math.factorial(steps_1 + steps_2) // (math.factorial(steps_1) * math.factorial(steps_2))
