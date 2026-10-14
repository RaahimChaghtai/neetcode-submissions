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

        # Phase 1: Traverse the graph and create a "shell" clone for each node
        while stk:
            node = stk.pop()

            # Map the original node to its new clone (value only, no neighbors yet)
            clones[node] = Node(node.val)

            for neigh in node.neighbors:
                if neigh not in visited:
                    visited.add(neigh)
                    stk.append(neigh)
        
        # Phase 2: Wire up the cloned nodes by mapping original neighbors to their new clones
        for oldNode, newNode in clones.items():
            for neigh in oldNode.neighbors:

                # Look up the clone of the neighbor from our dictionary
                new_neigh = clones[neigh]

                # Attach the cloned neighbor to the current clone's list
                newNode.neighbors.append(new_neigh)
        
        # Return the clone of the starting node
        return clones[startNode]

            




        