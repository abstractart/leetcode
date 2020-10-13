class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        
        rem = 1
        for i in range(len(digits)):
            value = digits[i] + rem
            rem = value // 10
            digits[i] = value % 10
        
        if rem > 0: digits.append(rem)
        
        digits.reverse()
        return digits
