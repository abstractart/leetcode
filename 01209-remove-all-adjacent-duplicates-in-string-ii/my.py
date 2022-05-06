class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        buffer = []
        
        i = 0
        while(i < len(s)):
            if not buffer:
                buffer.append([s[i], 1])
            elif s[i] != buffer[-1][0]:
                buffer.append([s[i], 1])
            else:
                buffer[-1][1] += 1
        
                if buffer[-1][1] == k:
                    buffer.pop()
            
            i += 1
           
        result = []
        for c, count in buffer:
            result.append(c * count)
        
        return "".join(result)
