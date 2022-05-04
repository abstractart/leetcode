from math import log

# O(n * log(n)) time complexity
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]         
        for i in range(1, n + 1):
            modulo = 2 ** int(log(i, 2))

            result.append(1 + result[i % modulo])
            
        return result
