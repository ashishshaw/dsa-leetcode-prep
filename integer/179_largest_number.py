#Approach: Convert the integers to strings and sort them based on a custom comparison function that compares the concatenated results of two numbers in both possible orders.
# If the concatenation of a followed by b is greater than b followed by a, then a should come before b in the sorted order. 
# After sorting, concatenate the numbers to form the largest number. 
# Finally, handle the case where the result is all zeros by returning "0" instead of "000...".

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0

        nums.sort(key=cmp_to_key(compare))

        result = ''.join(nums)

        return '0' if result[0] == '0' else result