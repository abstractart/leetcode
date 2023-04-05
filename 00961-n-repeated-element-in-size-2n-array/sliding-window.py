class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in  range(len(nums) - 3):
            if nums[i] == nums[i + 1] or nums[i] == nums[i + 2] or nums[i] == nums[i + 3]:
                return nums[i]
            elif nums[i + 1] == nums[i + 2] or nums[i + 1] == nums[i + 3]:
                return nums[i + 1]
            elif nums[i + 2] == nums[i + 3]:
                return nums[i + 2]
