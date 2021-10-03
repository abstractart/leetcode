class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c_to_i = {"1": 1, "0": 0}
        i_to_c = ["0", "1"]
        
        diff = abs(len(a) - len(b))
        
        if len(a) < len(b):
            a = "0" * diff + a
        else:
            b = "0" * diff + b
        
        stack = []
        remainder = 0
        for i in reversed(range(len(a))):
            s = c_to_i[a[i]] + c_to_i[b[i]] + remainder
            
            stack.append(i_to_c[s % 2])
            remainder = s // 2
            
        if remainder:
            stack.append(i_to_c[remainder])
        
        stack.reverse()
        
        
        return "".join(stack)
