class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        buffer = []
        
        for c in s:
            if buffer and c == buffer[-1][0]:
                buffer[-1][1] += 1
        
                if buffer[-1][1] == k:
                    buffer.pop()
            else:
                buffer.append([c, 1])

        return "".join([c * count for c, count in buffer])
