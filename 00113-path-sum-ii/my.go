func pathSum(root *TreeNode, targetSum int) [][]int {
    var result [][]int
    
    result = helper(root, targetSum, []int{}, result)
    
    return result
}

func helper(root *TreeNode, targetSum int, curr []int, result [][]int)[][]int {
    if root == nil {
        return result
    }
    curr = append(curr, root.Val)
    if root.Left == nil && root.Right == nil && root.Val == targetSum {
        s := make([]int, len(curr))
        
        copy(s, curr)
        result = append(result, s)
    } else {
        result = helper(root.Left, targetSum - root.Val, curr, result)
        result = helper(root.Right, targetSum - root.Val, curr, result)
    }
    
    return result
}
