class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while(low <= high):    
            m = low + (high - low) // 2
            
            if nums[m] == target: return m
            elif nums[m] > target:
                high = m - 1
            else:
                low = m + 1

        return -1
