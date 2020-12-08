class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        
        d = dict()
        for i in range(len(time)):
            time[i] %= 60
            if time[i] not in d: d[time[i]] = set()
                
            d[time[i]].add(i)
        
        for i, t in enumerate(time):
            pair = (60 - t) % 60
            if pair not in d: continue
            
            for index in d[pair]:
                if index >= i: continue
                
                count += 1
            
            
        return count
                
                
