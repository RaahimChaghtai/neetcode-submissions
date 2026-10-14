from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic_q = deque()
        atlantic_visited = set()

        pacific_q = deque()
        pacific_visited = set()

        rows = len(heights)
        cols = len(heights[0])

        
        for j in range(cols):
            pacific_q.append((0,j))
            pacific_visited.add((0,j))
        for i in range(1, rows):
            pacific_q.append((i,0))
            pacific_visited.add((i,0))

        for i in range(rows):
            atlantic_q.append((i, cols - 1))
            atlantic_visited.add((i, cols - 1))

        for j in range(cols - 1):
            atlantic_q.append((rows - 1,j))
            atlantic_visited.add((rows - 1,j))
        
        def get_coords(que, seen):
            coords = set()

            while que:
                i,j = que.popleft()

                for i_offset, j_offset in [(0,1), (1,0), (0,-1), (-1,0)]:
                        row, col = i + i_offset, j + j_offset
                        
                        if 0 <= row < rows and 0 <= col < cols and heights[row][col] >= heights[i][j] and (row, col) not in seen:
                            seen.add((row, col))
                            que.append((row, col))
        
        get_coords(pacific_q, pacific_visited)
        get_coords(atlantic_q, atlantic_visited)

        return list(pacific_visited.intersection(atlantic_visited))
                            


         
        