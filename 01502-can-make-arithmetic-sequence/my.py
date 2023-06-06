class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != arr[1] - arr[0]:
                return False

        return True
