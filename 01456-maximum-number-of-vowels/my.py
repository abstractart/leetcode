class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = frozenset('aeiou')
        maximum = float('-inf')
        
        dp = [0]
        for i in range(k):
            if s[i] in vowels:
                dp[0] += 1

        maximum = max(maximum, dp[0])

        for i in range(1, len(s) - k + 1):
            previous = dp[i - 1]
            if s[i - 1] in vowels:
                previous -= 1

            if s[i + k - 1] in vowels:
                previous += 1


            dp.append(previous)
            maximum = max(maximum, previous)

        return maximum
