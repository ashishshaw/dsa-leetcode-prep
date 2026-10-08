#Approach: Use a two-pointer technique to remove duplicates in-place. 
# Maintain a pointer k for the position of the next unique element. 
# Iterate through the array, and for each element, check if it can be placed at position k based on the allowed number of duplicates (in this case, 2). 

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for num in nums:
            if k < 2 or num != nums[k - 2]:
                nums[k] = num
                k += 1

        return k