class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
