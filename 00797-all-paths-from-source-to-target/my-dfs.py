class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        curr = (0, [], set())
        stack = [curr]
        paths = []
        while(len(stack) > 0):
            node, path, visited = stack.pop()
            
            visited.add(node)
            path.append(node)
            
            if node == len(graph) -1:
                paths.append(path)
                continue
            

            for n in graph[node]:
                if n not in visited:
                    stack.append((n, list(path), set(visited)))
            
        return paths
