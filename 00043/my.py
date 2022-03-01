class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.convert(num1) * self.convert(num2))
    
    def convert(self, num: str) -> list[int]:
        zero = ord('0')
        result = 0
        multiplier = 1
        
        for n in reversed(num):
            result += (ord(n) - zero) * multiplier
            multiplier *= 10
        
        return result
