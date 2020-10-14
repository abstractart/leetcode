class Solution:
    def sortedArrayToBST(self, nums):
        return self.recursive(nums, 0, len(nums) - 1)
        
        
    def recursive(self, nums, start, finish):
        if start > finish: return
        
        if start == finish: return TreeNode(nums[start])
        
        middle = (finish + start) // 2
        
        root = TreeNode(nums[middle])
        
        root.left = self.recursive(nums, start, middle - 1)
        root.right = self.recursive(nums, middle + 1, finish)
    
        return root
        
