# Define cases where it needs to stop (return), i.e target attained / overflow
# Backtracking std: Choose, Backtrack, Pop, Next

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()

        backtrack(0)
        return res
    
