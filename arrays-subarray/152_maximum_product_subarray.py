# a negative number can turn the smallest product into the largest product.
# So at every position, need to track:
# curMax: maximum product ending at current index
# curMin: minimum product ending at current index

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = cur_max = ans = nums[0]

        for num in nums[1:]:
            prev_min, prev_max = cur_min, cur_max

            cur_min = min(num, num*prev_min, num*prev_max)
            cur_max = max(num, num*prev_min, num*prev_max)

            ans = max(ans, cur_max)
   
        return ans


        