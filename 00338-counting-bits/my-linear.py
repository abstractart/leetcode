class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        if n >= 0:
            result.append(0)
        
        if n >= 1:
            result.append(1)
        
        power = 0
        value = 1
        for i in range(2, n + 1):
            if i / value == 2:
                value = i
                power += 1
            
            k = i - value
            result.append(1 + result[k])
            
        return result
