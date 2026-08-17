#Approach: Use DP where dp[j] stores the number of ways to reach the current cell; each cell gets top + left ways.
#Initialize dp = [1] * n and update with dp[j] += dp[j-1]; the answer is dp[n-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[n - 1]