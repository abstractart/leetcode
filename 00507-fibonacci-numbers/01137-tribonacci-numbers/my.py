class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        

        v = [0, 1, 1]


        for i in range(3, n + 1):
            nextVal = sum(v)

            v[0] = v[1]
            v[1] = v[2]
            v[2] = nextVal

        
        return v[2]
