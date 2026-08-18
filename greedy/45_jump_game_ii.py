#approach: Use a greedy algorithm to keep track of the farthest index that can be reached at each step.
#Then increment the jump count whenever we reach the end of the current jump range, 
#and update the current jump range to the farthest index that can be reached from the current position.

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps