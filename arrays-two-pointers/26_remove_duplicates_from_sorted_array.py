#Approach: Use two pointers to solve this problem. 
# We will maintain a slow pointer that points to the last unique element in the array, and a fast pointer that traverses the array. 
# When the fast pointer finds a new unique element, we will increment the slow pointer and update the value at the slow pointer 
# to be the new unique element. Finally, we will return the length of the unique elements, 
# which is given by the position of the slow pointer plus one.

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]


# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        n = len(nums)
        for j in range(1,n):
            if nums[i] != nums[j]:
                i += 1
            nums[i] = nums[j]

        return i+1
        