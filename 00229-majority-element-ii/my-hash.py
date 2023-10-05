from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        r = []
        for num, count in  Counter(nums).items():
            if count > len(nums) // 3:
                r.append(num)
        
        return r
