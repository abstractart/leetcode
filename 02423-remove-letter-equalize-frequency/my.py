from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        stats = {}
        for c, count in Counter(word).items():
            if count not in stats:
                stats[count] = 0
            stats[count] += 1

            if len(stats) > 2:
                return False
        
        if len(stats) == 1:
            return list(stats.keys())[0] == 1 or list(stats.values())[0] == 1
        
        max_frequency = max(stats.keys())
        min_frequency = min(stats.keys())
        
        return (max_frequency - min_frequency == 1 and stats[max_frequency] == 1) or (min_frequency == 1 and stats[min_frequency] == 1)
