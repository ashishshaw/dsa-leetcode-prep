# We keep track of the farthest index we can reach as we iterate through the array.
# If at any point the current index is greater than the farthest index we can reach,
# we return False. If we can reach the end of the array, we return True.

def canJump(self, nums: List[int]) -> bool:
    farthest = 0

    for i in range(len(nums)):
        if i > farthest:
            return False

        farthest = max(farthest, i + nums[i])

    return True