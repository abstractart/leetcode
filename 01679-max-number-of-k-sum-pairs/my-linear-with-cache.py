from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cache = Counter(nums)
        result = 0
        for left in cache:
            right = k - left
            if right in cache:
                if right == left:
                    result += cache[left] // 2
                else: 
                    result += min(cache[left], cache[right])
                    cache[right] = 0
                
                cache[left] = 0

                
        return result
