from math import log

# O(n * log(n)) time complexity
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]         
        for i in range(1, n + 1):
            p = int(log(i, 2))
            k = i - 2 ** p

            result.append(1 + result[k])
            
        return result
