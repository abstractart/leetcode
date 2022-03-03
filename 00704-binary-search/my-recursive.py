class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.recursive(nums, target, 0, len(nums) - 1)
    
    def recursive(self, nums, target, start, finish):
        if start > finish: return -1
        
        middle = start + ((finish - start) // 2)
        value = nums[middle]
        
        if value == target: return middle
        if value < target: return self.recursive(nums, target, middle + 1, finish)
        if value > target: return self.recursive(nums, target, start, middle - 1)
