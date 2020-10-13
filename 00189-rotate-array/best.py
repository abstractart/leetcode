class Solution:
    def rotate(self, nums, k):
        k %= len(nums)
        nums.reverse()
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        
    def reverse(self, nums, l, r):
        while(l < r):
            nums[l], nums[r]  = nums[r], nums[l]
            l += 1
            r -= 1
        
        
