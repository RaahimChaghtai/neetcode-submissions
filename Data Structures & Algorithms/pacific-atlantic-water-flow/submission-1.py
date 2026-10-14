from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # TIME - O(ROWS X COLS) 
        # SPACE - O(ROWS X COLS) 
        # Queues and visited sets for tracking reachability from each ocean
        atlantic_q = deque()
        atlantic_visited = set()

        pacific_q = deque()
        pacific_visited = set()

        rows = len(heights)
        cols = len(heights[0])

        # Step 1: Initialize the Pacific Ocean borders (Top row and Left column)
        # We start *from* the water and flow *inward* to find reachable land cells.
        for j in range(cols):
            pacific_q.append((0, j))
            pacific_visited.add((0, j))
        for i in range(1, rows):
            pacific_q.append((i, 0))
            pacific_visited.add((i, 0))

        # Step 2: Initialize the Atlantic Ocean borders (Right column and Bottom row)
        for i in range(rows):
            atlantic_q.append((i, cols - 1))
            atlantic_visited.add((i, cols - 1))

        for j in range(cols - 1):
            atlantic_q.append((rows - 1, j))
            atlantic_visited.add((rows - 1, j))
        
        # Helper function to perform BFS/traversal from the ocean borders inward.
        # Water can flow upward in elevation if we move backwards from the ocean (heights[row][col] >= heights[i][j]).
        def get_coords(que, seen):
            while que:
                i, j = que.popleft()

                # Check all 4 directions (Right, Down, Left, Up)
                for i_offset, j_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    row, col = i + i_offset, j + j_offset
                    
                    # Validate boundaries, check if the neighbor can flow to this ocean, and ensure it's unvisited
                    if (0 <= row < rows and 0 <= col < cols and 
                        heights[row][col] >= heights[i][j] and 
                        (row, col) not in seen):
                        
                        seen.add((row, col))
                        que.append((row, col))
        
        # Step 3: Run the traversal for both oceans independently
        get_coords(pacific_q, pacific_visited)
        get_coords(atlantic_q, atlantic_visited)

        # Step 4: Find the intersection of cells that can reach BOTH oceans
        return list(pacific_visited.intersection(atlantic_visited))