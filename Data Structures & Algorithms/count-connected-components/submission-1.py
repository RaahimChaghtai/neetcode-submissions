from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        count = 0
        visited = set()
        
        def dfs(node):
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh)
            
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count

            