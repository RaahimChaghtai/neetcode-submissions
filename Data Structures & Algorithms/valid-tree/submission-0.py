from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node):
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh)
        
        dfs(0)

        return len(visited) == n