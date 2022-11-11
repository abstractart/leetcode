class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] > nums[k]:
                k += 1
                nums[k]  = nums[i]

        return k + 1
