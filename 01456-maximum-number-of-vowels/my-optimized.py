class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = frozenset('aeiou')
        maximum = float('-inf')
        
        current = 0
        for i in range(k):
            if s[i] in vowels:
                current += 1

        maximum = max(maximum, current)

        for i in range(1, len(s) - k + 1):
            previous = current
            
            if s[i - 1] in vowels:
                previous -= 1

            if s[i + k - 1] in vowels:
                previous += 1

            maximum = max(maximum, previous)
            current = previous

        return maximum
