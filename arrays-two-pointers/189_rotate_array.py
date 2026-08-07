#Approach: We can rotate the array in place by reversing parts of the array. 
# First, we reverse the entire array, then we reverse the first k elements, 
# and finally, we reverse the remaining n-k elements. This effectively rotates the array to the right by k steps.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        