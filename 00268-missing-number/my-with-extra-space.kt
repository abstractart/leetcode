class Solution {
    fun missingNumber(nums: IntArray): Int {
        return (0..(nums.size)).toList().toIntArray().sum() - nums.sum()
    }
}
