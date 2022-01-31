class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        a = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",
            "...-",".--","-..-","-.--","--.."
        ]
        
        t = set()
        
        for w in words:
            t.add(self.transform(w, a))
        
        return len(t)
    
    def transform(self, w, a):
        result = []
        for c in w:
            result.append(a[ord(c) - 97])
            
        return "".join(result)
            
