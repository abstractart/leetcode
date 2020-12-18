class Solution:
    def checkValidString(self, s):
        max_open, min_open = 0, 0

        for c in s:
            if c == '(': 
              min_open += 1  
            else: min_open -= 1
            
            if c != ')': 
              max_open += 1  
            else: max_open -= 1

            if max_open < 0: return False
            min_open = max(0, min_open)

        return min_open == 0
