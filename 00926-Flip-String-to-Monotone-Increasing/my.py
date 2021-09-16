class Solution(object):
    def minFlipsMonoIncr(self, s):
        ones = 0
        zeros = 0
        flips = 0
        
        for c in s:
            if c == '0':
                if ones > 0:
                    flips += 1
                    ones -= 1
                else:
                    zeros += 1
            if c == '1':
                ones += 1
        return flips
