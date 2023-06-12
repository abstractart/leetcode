class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []

        i = 0
        while(i < len(nums)):
            j = i

            while(j + 1 < len(nums)):
                if nums[j + 1] - nums[j] == 1:
                    j += 1
                else:
                    break

            if i == j:
                output.append(f"{nums[i]}")
            else:
                output.append(f"{nums[i]}->{nums[j]}")
            
            i = j + 1

        
        return output
