#Approach: We use a hashmap to store the first occurrence of each prefix sum. 
# For each element, we calculate the prefix sum and check if (prefix_sum - k) exists in the hashmap. 
# If it does, it means there is a subarray with sum k.

# Input:
# nums = [1, -1, 5, -2, 3]
# k = 3

# Output:
# [1, -1, 5, -2]
# Length = 4



class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        res = 0
        prefix_map = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += num

            rem = prefix_sum - k

            if rem in prefix_map:
                res = max(res, i - prefix_map[rem])

            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        return res
