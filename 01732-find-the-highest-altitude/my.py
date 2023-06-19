class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        curr = 0
        for g in gain:
            curr += g
            
            altitude = max(altitude, curr)
        return altitude
