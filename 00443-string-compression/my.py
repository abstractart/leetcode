class Solution:
    def compress(self, chars: List[str]) -> int:
        length = 0
        count = 1
        chars.append("\n")
        
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
                continue
            
            # Write char
            chars[length] = chars[i - 1]
            length += 1
            
            if count == 1: continue
            # Write digis
            for n in str(count):
                chars[length] = n
                length += 1
            
            # Reset counter
            count = 1
            
        return length
