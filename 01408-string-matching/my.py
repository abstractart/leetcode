class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        r = set()

        for candidate in words:
            for word in words:
                if candidate != word and candidate in word:
                    r.add(candidate)
        
        return list(r)
