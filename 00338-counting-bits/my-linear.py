class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        
        if n >= 1:
            result.append(1)
        
        modulo = 1
        for i in range(2, n + 1):
            if i / modulo == 2:
                modulo = i
            
            result.append(1 + result[i % modulo])
            
        return result
