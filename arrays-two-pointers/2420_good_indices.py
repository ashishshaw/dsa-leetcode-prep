class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # left[i] = length of non-increasing run ending at i
        left = [1] * n
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                left[i] = left[i - 1] + 1

        # right[i] = length of non-decreasing run starting at i
        right = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                right[i] = right[i + 1] + 1

        ans = []
        for i in range(k, n - k):
            if left[i - 1] >= k and right[i + 1] >= k:
                ans.append(i)

        return ans