#Approach: First, we handle the base cases where n is 2 or 3. 
# For n > 4, we repeatedly subtract 3 and multiply the result by 3 until n is less than or equal to 4. 
# Then we multiply the result by the remaining value of n.

# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.



class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        product = 1

        while n > 4:
            product *= 3
            n -= 3

        product *= n

        return product