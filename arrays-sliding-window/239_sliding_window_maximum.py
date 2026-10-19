#Approach: Use a deque to maintain indices of elements in the current window, ensuring the maximum element is always at the front.

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i in range(len(nums)):

            # Remove indices outside the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller values from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # First window is complete
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans