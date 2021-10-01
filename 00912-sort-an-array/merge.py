class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 2:
            return merge(
                self.sortArray(nums[:len(nums) // 2]),
                self.sortArray(nums[len(nums) // 2:])
            )
        
        return sorted(nums)
    
    
    def merge(self, a, b):
        r = [None] * len(a) + len(b)
        i, j, k  = 0, 0, 0
        
        while(i < len(a) and j < len(b)):
            if a[i] < b[i]:
                r[k] = a[i]
                i += 1
            else:
                r[k] = b[j]
                j += 1
            
            k += 1
           
        while(i < len(a)):
            r[k] = a[i]
            i += 1
            k += 1
            
        while(i < len(b)):
            r[k] = b[j]
            j += 1
            k += 1
         
        return r
