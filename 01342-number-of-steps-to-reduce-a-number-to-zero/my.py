class Solution:
    def numberOfSteps (self, num: int) -> int:
        b = list(format(num, "b"))
        count = 0
        
        while(True):
            if len(b) == 1 and b[0] == "0": return count

            if b[-1] == "1":
                b[-1] = "0"
            else:
                b.pop()
            
            count += 1
