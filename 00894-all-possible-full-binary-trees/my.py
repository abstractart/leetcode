class Solution:
    def allPossibleFBT(self, n: int):
        if n % 2 == 0:
            return []

        acc = {}
        acc[0] = [None]
        acc[1] = [TreeNode(0)]

        self.helper(n, acc)
        return acc[n]


    def helper(self, n, acc):
        if n in acc:
            return acc[n]

        trees = []
        leftCount = 1
        while(leftCount <= n - 2):
            rightCount = n - leftCount - 1

            leftTrees = self.helper(leftCount, acc)
            rightTrees = self.helper(rightCount, acc)
            for l in leftTrees:
                for r in rightTrees:
                    trees.append(TreeNode(0, l, r))

            leftCount += 2
        
        acc[n] = trees
        return acc[n]
