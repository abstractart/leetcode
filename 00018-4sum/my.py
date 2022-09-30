from collections import Counter

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        counts = Counter(nums)
        nums.sort()
        
        solutions = set()
        for i in range(len(nums) - 3):
            if counts[nums[i]] > 4:
                counts[nums[i]] -= 1
                continue
            
            threeSumSolutions = self.threeSumTarget(nums[i + 1:], target - nums[i])
            for tSumSol in threeSumSolutions:                
                solutions.add(tSumSol + (nums[i],))
                
            
        return list(solutions)
            

    def threeSumTarget(self, nums, target):
        result = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            
            l, r = i + 1, n - 1
            twoSumTarget = target - nums[i]
            
            while(l < r):
                if nums[l] + nums[r] == twoSumTarget:
                    result.append((nums[i], nums[l], nums[r]))
                    
                    l += 1
                    while(l < n and nums[l] == nums[l - 1]): l += 1
                    
                    r -= 1
                    while(r >= 0 and nums[r] == nums[r + 1]): r -= 1
                elif nums[l] + nums[r] < twoSumTarget:
                    l += 1
                else:
                    r -= 1
                
        return result
