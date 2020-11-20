class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        count = 1
        prev = chars[0]
        chars.append("\n")
        
        for i in range(1, len(chars)):
            c = chars[i]
            if c == prev: count += 1
            else:
                chars[index] = prev
                index += 1
                
                if count > 1:
                    for n in map(int, str(count)):
                        chars[index] = str(n)
                        index += 1
                    
                    count = 1
            
            prev = c
        return index
