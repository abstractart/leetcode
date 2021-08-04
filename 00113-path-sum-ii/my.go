func pathSum(root *TreeNode, targetSum int) [][]int {
    var result [][]int
    
    result = helper(root, targetSum, make([]int, 0), result)
    
    return result
}

func helper(root *TreeNode, targetSum int, curr []int, result [][]int)[][]int {
    if root == nil {
        return result
    }
    if root.Left == nil && root.Right == nil && root.Val == targetSum {
        result = append(result, append(curr, root.Val))
    } else {
        currForLeft := make([]int, len(curr))
        copy(currForLeft, curr)
        currForLeft = append(currForLeft, root.Val)
        
        currForRight := make([]int, len(curr))
        copy(currForRight, curr)
        currForRight = append(currForRight, root.Val)
        
        result = helper(root.Left, targetSum - root.Val, currForLeft, result)
        result = helper(root.Right, targetSum - root.Val, currForRight, result)
    }
    
    return result
}
