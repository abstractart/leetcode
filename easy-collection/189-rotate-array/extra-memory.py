class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        rotated = [None] * len(nums)
        
        for i in range(len(nums)):
            new_index = (i + k) % len(nums)
            rotated[new_index] = nums[i]
            
        for i in range(len(nums)):
            nums[i] = rotated[i]
            
        
        
        
