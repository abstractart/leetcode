class Solution:
    def levelOrder(self, root):
        acc = []
        
        stack = []
        if root: stack.append([root])
        
        while(len(stack) > 0):
            nodes = stack.pop()
            
            values = []
            for n in nodes:
                values.append(n.val)
            
            acc.append(values)
            
            newNodes = []
            for n in nodes:
                if n.left: newNodes.append(n.left)
                if n.right: newNodes.append(n.right)
            
            if len(newNodes) > 0: stack.append(newNodes)

        return acc
