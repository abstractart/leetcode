# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.helper(1, n)
    

    def helper(self, l, r):
        m = l + (r - l) // 2
        v = guess(m)
        
        if v == 0:
            return m
        
        if v < 0:
            return self.helper(l, m - 1)
        if v > 0:
            return self.helper(m + 1, r)
