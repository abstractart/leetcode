class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.search(nums, target, 0, len(nums) - 1)
    
    def search(self, nums, target, start, end):
        if start > end: return end + 1
            
        middle = start + (end - start) // 2
        
        if target > nums[middle]:
            return self.search(nums, target, middle + 1, end)
        if target < nums[middle]:
            return self.search(nums, target, start, middle - 1)
        
        return middle
