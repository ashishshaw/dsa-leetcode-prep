#Approach: Dynamic Programming (Space Optimized)
#We use a 1D array to store the number of ways to reach each cell in the current row.
#If a cell contains an obstacle, we set the number of ways to 0.
#Otherwise, we update the number of ways by adding the number of ways from the left cell.

# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [0] * n
        dp[0] = 1

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c>0:
                    dp[c] += dp[c - 1]

        return dp[-1]