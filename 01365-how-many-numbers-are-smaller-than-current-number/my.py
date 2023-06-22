class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        copyNums = [n for n in nums]
        copyNums.sort()

        stats = {}


        i = 0

        while(i < len(copyNums)):
            j = i

            while(j < len(nums) and copyNums[j] == copyNums[i]):
                j+= 1
            
            stats[copyNums[i]] = i

            i = j
            

        r = []
        for n in nums:
            r.append(stats[n])

        return r
