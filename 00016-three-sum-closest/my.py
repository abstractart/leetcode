class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        solution = float('inf')
        for i in range(len(nums)):
            a = nums[i]
            
            j, k = i + 1, len(nums) - 1
            while(j < k):
                b, c = nums[j], nums[k]
                if abs(solution - target) > abs((a + b + c) -  target):
                    solution = a + b + c
                
                if (a + b + c) > target:
                    k -= 1
                else:
                    j += 1
        
        return solution
