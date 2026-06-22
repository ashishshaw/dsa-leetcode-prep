#Compare nums[mid] with nums[mid + 1].
#  If the slope is increasing, a peak must exist on the right side, so move right. 
# If the slope is decreasing, a peak must exist at mid or on the left side, so move left. 
# Repeating this binary search eventually converges to a peak element in O(log n) time.

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