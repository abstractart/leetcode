class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexesMap = {}

        for i, n in enumerate(nums):
            if n not in indexesMap:
                indexesMap[n] = []
            
            indexesMap[n].append(i)
        

        for n, indexes in indexesMap.items():
            for i in range(len(indexes) - 1):
                if abs(indexes[i] - indexes[i + 1]) <= k:
                    return True
        
        return False

