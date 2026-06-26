#Checking if the houses are in a circle, we can either rob the first house or the last house, but not both. 
# So we can break the problem into two subproblems: robbing from the first house to the second last house, 
# and robbing from the second house to the last house. We can then take the maximum of these two subproblems.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(
            self.robLinear(nums[:-1]),  # Exclude last house
            self.robLinear(nums[1:])    # Exclude first house
        )

    def robLinear(self, nums):
        prev1 = 0  # Maximum amount up to previous house
        prev2 = 0  # Maximum amount up to house before previous

        for num in nums:
            curr = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = curr

        return prev1