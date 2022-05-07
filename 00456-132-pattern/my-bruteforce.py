class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] >= nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[i] < nums[k] and nums[k] < nums[j]:
                        return True
                    
        return False
        
