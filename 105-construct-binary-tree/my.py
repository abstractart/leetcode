class Solution:
    def buildTree(self, preorder, inorder):
        p = {}
        
        for index, e in enumerate(preorder):
            p[e] = index
        
        i = {}
        for index, e in enumerate(inorder):
            i[e] = index

        return self.helper(preorder, inorder, 0, len(preorder), 0, len(inorder), p, i)

    def helper(self, preorder, inorder, p_start, p_finish, i_start, i_finish, p, i):
        if not range(p_start, p_finish):
            return None
        
        root_val = preorder[p_start]
        root_index_inorder = i[root_val]
        
        node = TreeNode(root_val)
        left_size = root_index_inorder - i_start
        if left_size > 0:
            node.left = self.helper(
                preorder,
                inorder,
                p_start + 1, p_start + 1 + left_size,
                i_start, root_index_inorder,
                p, i
            )
        
        right_size = len(inorder) - left_size - 1
        if right_size > 0:
            node.right = self.helper(
                preorder,
                inorder,
                p_start + 1 + left_size, p_finish, 
                root_index_inorder + 1, i_finish, 
                p, i
            )
            
        
        return node
