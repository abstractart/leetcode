class Solution:
    def isThree(self, n: int) -> bool:
        divisors_count = 2
        
        for i in range(2, n // 2 + 1):
            if not n % i:
                divisors_count += 1
        
        return divisors_count == 3
