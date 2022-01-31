class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        
        while(n > 0):
            bits.append(n % 2)
            n //= 2
        
        while(len(bits) < 32):
            bits.append(0)
            
        multiplier = 1
        result = 0
        for i in reversed(range(len(bits))):
            result += bits[i] * multiplier
            
            multiplier *= 2
            
        return result
