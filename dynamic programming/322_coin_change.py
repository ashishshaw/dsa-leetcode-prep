# We iterate through each amount from 1 to the target amount. For each amount, we iterate through each coin denomination. 
# If the current amount is greater than or equal to the coin denomination, we update the dp array at the current amount index 
# with the minimum of its current value and the value at the index of the current amount minus the coin denomination plus 1 (which represents using one more coin).
#Finally, we return the value at dp[amount] if it is not infinity, indicating that it is possible to make change for the target amount. If it is still infinity

import math
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [(math.inf)] * (amount+1) 
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i>=coin:
                    dp[i] = min(dp[i], 1+dp[i-coin])

        return dp[amount] if dp[amount] != math.inf else -1
    