# Define cases where it needs to stop (return), i.e target attained / overflow
# Backtracking std: Choose, Backtrack, Pop, Next

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def backtrack(index, curr, total):
            
            if total == target:
                res.append(curr[:])
                return

            if total > target or index>=len(candidates):
                return 
            
            curr.append(candidates[index])
            backtrack(index, curr, total+candidates[index])
            curr.pop()

            backtrack(index+1, curr, total)

        backtrack(0, [], 0)
        return res
    