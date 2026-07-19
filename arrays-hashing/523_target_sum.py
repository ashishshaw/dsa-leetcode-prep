class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_index = {0: -1}
        prefix = 0

        for i, num in enumerate(nums):
            prefix = (prefix + num) % k

            if prefix in remainder_index:
                if i - remainder_index[prefix] > 1:
                    return True
            else:
                remainder_index[prefix] = i

        return False