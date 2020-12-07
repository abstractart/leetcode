class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        flowerbed.insert(0, 0)
        
        index = 1
        while(n > 0 and index < len(flowerbed) - 1):
            if self.canPlaceFlower(flowerbed, index):
                flowerbed[index] = 1
                n -= 1
                index += 2
            else:
                index += 1
                
        
        return n == 0
                
        
            
    def canPlaceFlower(self, flowerbed, index):
        return flowerbed[index + 1] == 0 and flowerbed[index] == 0 and flowerbed[index - 1] == 0
