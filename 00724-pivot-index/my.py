class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)

        curr = 0
        for i in range(len(nums)):
            if (s - nums[i]) % 2 == 0 and (s - nums[i]) // 2 == curr:
                return i
            
            curr += nums[i]
        
        return -1
