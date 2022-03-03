class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diff = []
        
        for i in range(1, len(nums)):
            diff.append(nums[i] - nums[i - 1])
            
        count = 0
        i = 0

        while(i < len(diff)):
            j = self.lastIndexWithSameValue(diff, i)
            if j != i:
                sequenceSize = j - i + 1
                for k in range(2, sequenceSize + 1):
                    count += sequenceSize - k + 1
            
            i = j + 1
                
        return count
        
    def lastIndexWithSameValue(self, diff, start):
        for i in range(start, len(diff)):
            if diff[i] != diff[start]: return i - 1 
        
        return len(diff) - 1
