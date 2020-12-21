class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index = m + n  - 1
        
        i1 = m - 1
        i2 = n - 1
        while(i2 >= 0 and i1 >= 0):
            if nums2[i2] > nums1[i1]:
                nums1[index] = nums2[i2]
                i2 -= 1
            else:
                nums1[index] = nums1[i1]
                i1 -= 1
                
            index -= 1
            
        if i1 < 0 and i2 >= 0:
            for i in range(i2, -1, -1):
                nums1[i] = nums2[i]
