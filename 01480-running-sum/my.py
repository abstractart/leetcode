class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0]
    
        for n in nums:
            result.append(result[-1] + n)
        return result[1:]
