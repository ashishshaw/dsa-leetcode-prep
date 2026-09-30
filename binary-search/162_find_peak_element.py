#Compare nums[mid] with nums[mid + 1].
#  If the slope is increasing, a peak must exist on the right side, so move right. 
# If the slope is decreasing, a peak must exist at mid or on the left side, so move left. 
# Repeating this binary search eventually converges to a peak element in O(log n) time.

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left