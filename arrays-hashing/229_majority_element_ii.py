#Store the count of each number in a hashmap and check if the count is greater than n/3

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        res = []
        num_map = Counter(nums)
        for key, val in num_map.items():
            if val > threshold:
                res.append(key)

        return res

        