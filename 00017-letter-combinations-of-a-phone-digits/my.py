class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        digits = list(digits)
        mapping = dict()
        mapping["2"] = ["a", "b", "c"]
        mapping["3"] = ["d", "e", "f"]
        mapping["4"] = ["g", "h", "i"]
        mapping["5"] = ["j", "k", "l"]
        mapping["6"] = ["m", "n", "o"]
        mapping["7"] = ["p", "q", "r", "s"]
        mapping["8"] = ["t", "u", "v"]
        mapping["9"] = ["w", "x", "y", "z"]
        
        state = [0] * len(digits)
        curr = len(digits) - 1
        indexes = list(range(len(digits)))
    
        result = []
        while(True):
            lst = list(map(lambda i: mapping[digits[i]][state[i]], indexes))
            s = "".join(lst)
            result.append(s)

            if not self.nextState(state, digits, mapping): break
                
                
            
        return result
    
    def nextState(self, state, digits, mapping):
        reminder = 1
        index = len(digits) - 1
        while(index >= 0 and reminder > 0):
            val = state[index] + reminder
            reminder = val // len(mapping[digits[index]])
            state[index] = val % len(mapping[digits[index]])
            
            index -= 1
            
        
        if reminder > 0: return None
        return True
