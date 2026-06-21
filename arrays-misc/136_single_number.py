#1st approach: Counter -> O(n) time and space
#2nd approach: XOR -> O(n) time and O(1) space

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        for key, val in num_count.items():
            if val == 1:
                return key
        return -1
    
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num

        return ans
        