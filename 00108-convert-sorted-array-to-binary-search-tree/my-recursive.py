class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums) - 1)
    
    
    def helper(self, nums, start, finish):
        if start > finish: return None
        
        middle = start + (finish - start) // 2
        
        node = ListNode(nums[middle])
        
        node.left = self.helper(nums, start, middle - 1)
        node.right = self.helper(nums, middle + 1, finish)
        
        return node
