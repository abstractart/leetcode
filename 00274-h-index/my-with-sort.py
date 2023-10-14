class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        if citations[-1] == 0:
            return 0

        h = 0
        for i in reversed(range(len(citations))):
            count = len(citations) - i
            
            candidate = min(count, citations[i])
            if candidate < h:
                break
            else:
                h = candidate

        return h
