class Solution:
    def pathSum(self, root, targetSum):
        if not root: return 0
        
        return self.pathSumRec(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
    
    
    def pathSumRec(self, root, targetSum):
        if not root: return 0

        result = 0
        if root.val == targetSum:
            result += 1
        
        return result + self.pathSumRec(root.left, targetSum - root.val) + self.pathSumRec(root.right, targetSum - root.val)
