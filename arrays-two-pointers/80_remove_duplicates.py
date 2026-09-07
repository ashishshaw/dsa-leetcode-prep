#Approach: Use a two-pointer technique to remove duplicates in-place. 
# Maintain a pointer k for the position of the next unique element. 
# Iterate through the array, and for each element, check if it can be placed at position k based on the allowed number of duplicates (in this case, 2). 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for num in nums:
            if k < 2 or num != nums[k - 2]:
                nums[k] = num
                k += 1

        return k