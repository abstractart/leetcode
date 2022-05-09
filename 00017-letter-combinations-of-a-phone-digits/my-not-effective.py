class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxyz"),
        }
        
        return self.helper(digits, mapping)
        
    def helper(self, digits, mapping):
        if len(digits) == 1:
            return mapping[digits[0]]
        
        result = []
        for r1 in mapping[digits[0]]:
            for r2 in self.helper(digits[1:], mapping):
                result.append(r1 + r2)
        
        return result
