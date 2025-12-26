import heapq
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        priority = []
        
        depends = {}
        unlocks = {}
        
        for n in range(numCourses):
            depends[n] = set()
            unlocks[n] = set()

        for course, requirement in prerequisites:        
            depends[course].add(requirement)
            unlocks[requirement].add(course)
        
        for k, v in depends.items():
            heapq.heappush(priority, (len(v), k))
        
        result = []
        
        while(len(result) < numCourses):
            v, k = heapq.heappop(priority)
            
            if v > 0:
                return []
            
            result.append(k)
            for parent in unlocks[k]:
                depends[parent].remove(k)
                heapq.heappush(priority, (len(depends[parent]), parent))
        
        return result
