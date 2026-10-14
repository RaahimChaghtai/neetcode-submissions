"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        startNode = node
        clones = {}
        stk = [startNode]
        visited = set()
        visited.add(startNode)

        while stk:
            node = stk.pop()
            clones[node] = Node(node.val)

            for neigh in node.neighbors:
                if neigh not in visited:
                    visited.add(neigh)
                    stk.append(neigh)
        
        for oldNode, newNode in clones.items():
            for neigh in oldNode.neighbors:
                new_neigh = clones[neigh]
                newNode.neighbors.append(new_neigh)
        
        return clones[startNode]

            




        