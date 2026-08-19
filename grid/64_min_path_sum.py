#Approach: Use dynamic programming to calculate the minimum path sum. 
# Iterate through the grid and update each cell with the minimum path sum to reach that cell from the top-left corner. 
# The value of each cell is updated based on the minimum of the cell above it and the cell to the left of it, 
# plus the current cell's value. Finally, return the value in the bottom-right corner of the grid, which represents the minimum path sum to reach that cell.


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]