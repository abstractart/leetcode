from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maximum = float("-inf")
        levelWithMax = None

        queue = deque()
        queue.append(root)
        
        currentLevel = 1
        while(queue):
            levelLength = len(queue)
            curr = 0
            for _ in range(levelLength):
                node = queue.popleft()
                curr += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if curr > maximum:
                levelWithMax = currentLevel
                maximum = curr
            
            currentLevel += 1
        return levelWithMax
