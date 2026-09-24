#Approach: Dynamic Programming (Space Optimized)
#First, we initialize two variables a and b to 1, representing the number of ways to reach the first and second steps.
# Then, we iterate from the third step to the nth step, updating a and b at each iteration.
# Finally, we return the value of b, which represents the number of ways to reach the nth step.

class Solution:
    def climbStairs(self, n: int) -> int:
        
        a,b = 1,1

        for _ in range(2,n+1):
            a,b= b,a+b

        return b
