#Approach: First, we create a dictionary to store the last seen index of each number in the array. 
# We then iterate through the array, and for each number, we check if it has been seen before a
# nd if the difference between the current index and the last seen index is less than or equal to k. 
# If both conditions are met, we return True. If we finish iterating through the array without finding any such pair, we return False.


# Input: nums = [1,2,3,1], k = 3
# Output: true

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True

            seen[num] = i
        
        return False