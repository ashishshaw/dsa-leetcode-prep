#Approach: We use three pointers to partition the array into three regions: 0s, 1s, and 2s. 

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid = 0, 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
        