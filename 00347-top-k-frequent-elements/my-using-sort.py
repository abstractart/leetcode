from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        
        values = []
        for num, count in counts.items():
            values.append((count, num))
        
        values.sort()
        
        r = []
        for i in range(k):
            _, num = values.pop()
            r.append(num)
        
        return r
