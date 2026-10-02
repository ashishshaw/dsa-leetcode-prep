#Approach: We use a hashmap to store the frequency of each prefix sum. 
# For each element, we calculate the prefix sum and check if (prefix_sum - k) exists in the hashmap. 
# If it does, it means there is a subarray with sum k.


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if nums is None:
            return 0

        res = 0
        prefix_sum = 0
        prefix_map = {0:1}

        for num in nums:
            prefix_sum += num
            rem = prefix_sum - k
            if rem in prefix_map:
                res += prefix_map[rem]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum,0) + 1

        return res