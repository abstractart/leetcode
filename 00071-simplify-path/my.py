class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        
        pathSegments = path.split("/")
                
        for pathSegment in pathSegments:
            if not pathSegment:
                continue
            if pathSegment == ".":
                continue
            if pathSegment == '..':
                if len(result) > 0:
                    result.pop()
            else:
                result.append(pathSegment)
        
        return "/" + "/".join(result)
