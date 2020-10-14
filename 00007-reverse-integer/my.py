class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        curr = abs(x)
        
        while(curr > 0):
            result = result * 10 + curr % 10
            curr //= 10
    
        if x < 0:
            result *= -1
        if result not in range(-2147483648, 2147483648): return 0
        return result
