#Classic approach with prefix and suffix products
#First, we calculate the prefix products for each element in the array and store them in a new array. 
#Then, we calculate the suffix products for each element in the array and multiply them with the corresponding prefix product to get the final result.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
    