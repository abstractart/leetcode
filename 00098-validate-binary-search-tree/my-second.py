class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        
        values = []
        self.LNROrder(root, values)
        
        return self.checkOrder(values)
        
        
    def LNROrder(self, root, acc):
        if not root: return
        
        if root.left: self.LNROrder(root.left, acc)
        
        acc.append(root.val)
        
        if root.right: self.LNROrder(root.right, acc)
            
        
    def checkOrder(self, arr):        
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]: return False
            
        return True
