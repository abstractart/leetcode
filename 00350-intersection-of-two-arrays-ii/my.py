from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        counts1, counts2 = Counter(nums1), Counter(nums2)
        
        result = []
        
        for k in counts1.keys():
            intersect_count = min(counts2.get(k, 0), counts1[k])
            for i in range(intersect_count):
                result.append(k)
        
        return result
