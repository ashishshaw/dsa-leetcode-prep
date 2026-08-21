#Approach: Use Depth First Search (DFS) to traverse the grid. Iterate through each cell in the grid, and when a '1' is found, 
# increment the island count and perform DFS to mark all connected '1's as '0's. This effectively "sinks" the island, 
# preventing it from being counted again.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return

            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands