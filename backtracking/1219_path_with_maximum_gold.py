# We can use backtracking to explore all possible paths in the grid.
# We start from each cell that contains gold and perform a depth-first search (DFS) to collect gold. 
# During the DFS, we mark the cell as visited by setting its value to 0, and we explore all four possible directions (up, down, left, right).


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0

            gold = grid[r][c]
            grid[r][c] = 0  # mark visited

            best = 0

            # 4 directions
            best = max(best, dfs(r + 1, c))
            best = max(best, dfs(r - 1, c))
            best = max(best, dfs(r, c + 1))
            best = max(best, dfs(r, c - 1))

            grid[r][c] = gold  # backtrack

            return gold + best

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0:
                    ans = max(ans, dfs(r, c))

        return ans