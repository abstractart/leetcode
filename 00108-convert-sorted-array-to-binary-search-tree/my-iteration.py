class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        s = []
        
        result = TreeNode(0)
        s.append((0, len(nums) - 1, result, True))
        
        while(s):
            start, finish, parent, position = s.pop()
            if start > finish:
                continue
                
            middle = start + (finish - start) // 2
            
            node = TreeNode(nums[middle])
            
            if position:
                parent.left = node
            else:
                parent.right = node
                
            s.append((start, middle - 1, node, True))
            s.append((middle + 1, finish, node, False))
            
            
        return result.left
