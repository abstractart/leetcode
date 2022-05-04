class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums) - 1):
            if not nums[i]:
                continue
            
            for j in range(i + 1, len(nums)):
                if not nums[j]:
                    continue

                if nums[i] + nums[j] == k:
                    count += 1
                    nums[i] = 0
                    nums[j] = 0    
                    break;
        return count
